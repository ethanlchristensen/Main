import pygame
import math
from queue import PriorityQueue
import time
import mazegen
from pygame.constants import GL_ACCELERATED_VISUAL

pixel_size = 2
ROWS = 500
my_maze = mazegen.maze(ROWS)
WIDTH = ROWS * pixel_size
WIN = pygame.display.set_mode((ROWS * pixel_size, ROWS * pixel_size))
pygame.display.set_caption('A* Path Finding ALgorithm')

RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    def __init__(self, row, col, width, rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.rows = rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREY

    def is_barrier(self):
        return self.color == BLACK

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def is_path(self):
        return self.color == PURPLE

    def is_final(self):
        return self.color == GREEN

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREY

    def make_start(self):
        self.color = ORANGE

    def make_end(self):
        self.color = TURQUOISE
    
    def reset(self):
        self.color = WHITE
    
    def make_barrier(self):
        self.color = BLACK

    def make_intermediate(self):
        self.color = YELLOW

    def make_path(self):
        self.color = PURPLE
    
    def make_final(self):
        self.color = GREEN

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbors(self, grid):
        self.neighbors = []
        if self.row < self.rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.row > 0 and not grid[self.row][self.col -  1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

def make_grid(rows, width):
    start = None
    end = None
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            if my_maze[i][j] == 'c' and i == 0:
                spot = Spot(i, j, gap, rows)
                spot.make_start()
                start = spot
                grid[i].append(spot)
            elif my_maze[i][j] == 'c' and i == ROWS - 1:
                spot = Spot(i, j, gap, rows)
                spot.make_end()
                end = spot
                grid[i].append(spot)
            elif my_maze[i][j] == 'w':
                spot = Spot(i, j, gap, rows)
                spot.make_barrier()
                grid[i].append(spot)
            elif my_maze[i][j] == 'c':
                spot = Spot(i, j, gap, rows) 
                grid[i].append(spot)    
    return grid, start, end

#def draw_grid(win, rows, width):
#    gap = width // rows
#    for i in range(rows):
#        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
#    for j in range(rows):
#        pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    pygame.display.update()

def path(came_from, current, win):
    while current in came_from:
        time.sleep(0.002)
        current = came_from[current]
        if not current.is_start() and not current.is_end():
            current.make_path()
            current.draw(win)
        pygame.display.update()

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def algorithm(grid, start, end, win, width):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())
    open_set_hash = {start}
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]
        open_set_hash.remove(current)
        if current == end:
            for row in grid:
                for spot in row:
                    if not spot.is_barrier() and not spot.is_start() and not spot.is_end():
                        spot.reset()   
            path(came_from, end, win)
            for row in grid:
                for spot in row:
                    if not spot.is_path() and not spot.is_barrier():
                        spot.reset()
                        spot.draw(win)
                pygame.display.update()
            end.make_end()
            return True
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    if not neighbor.is_end():
                        neighbor.make_open()
                        neighbor.draw(win)
            if current != start:
                current.make_closed()
                current.draw(win)
            pygame.display.update()     
    return False

def main(win, width):
    global my_maze
    grid, start, end = make_grid(ROWS, width)
    run = True
    started = False
    draw(win, grid)
    while run:
        draw(win, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started: continue
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for spot in row:
                            if not spot.is_barrier() and not spot.is_start() and not spot.is_end():
                                spot.reset()
                                spot.draw(win)
                    if start is None or end is None:
                        break
                    else:
                        for row in grid:
                            for spot in row:
                                spot.update_neighbors(grid)
                        algorithm(grid, start, end, win, width)
                if event.key == pygame.K_c:
                            for row in grid:
                                for spot in row:
                                    if not spot.is_barrier() and not spot.is_start() and not spot.is_end():
                                        spot.reset()
                if event.key == pygame.K_r:
                            my_maze = mazegen.maze(ROWS)
                            grid, start, end = make_grid(ROWS, width)
                            for row in grid:
                                for spot in row:
                                    if not spot.is_barrier() and not spot.is_start() and not spot.is_end():
                                        spot.reset()
                if event.key == pygame.K_q:
                            pygame.quit()        
        

main(WIN, WIDTH)