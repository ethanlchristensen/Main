import copy

def printGrid(inGrid, name):
    print("GRID:", name)
    for i in inGrid:
        print(i)



def orangesRotting(grid):
    prev = copy.deepcopy(grid)
    out = copy.deepcopy(grid)
    h = {}
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            h[(r,c)] = []
    print(h)
    def update():
        if len(prev) > 2:
            if len(prev[0]) > 2:
                for i in range(len(grid)):
                    for j in range(len(grid[i])):
                        if prev[i][j] == 2:
                                if i == 0 and j == 0: # TOP LEFT CORNER
                                    if prev[i + 1][j] == 1:
                                        out[i + 1][j] = 2
                                    if prev[i][j + 1] == 1:
                                        out[i][j + 1] = 2
                                elif i == 0 and j == len(prev[i]) - 1: # TOP RIGHT CORNER
                                    if prev[i + 1][j] == 1:
                                        out[i + 1][j] = 2
                                    if prev[i][j - 1] == 1:
                                        out[i][j - 1] = 2
                                elif i == len(prev) - 1 and j == 0: # BOTTOM LEFT CORNER
                                    if prev[i - 1][j] == 1:
                                        out[i - 1][j] = 2
                                    if prev[i][j + 1] == 1:
                                        out[i][j + 1] = 2
                                elif i == len(prev) - 1 and j == len(prev[i]) - 1: # BOTTOM RIGHT CORNER
                                    if prev[i - 1][j] == 1:
                                        out[i - 1][j] = 2
                                    if prev[i][j - 1] == 1:
                                        out[i][j - 1] = 2
                                elif i == 0 and j < len(prev[i]) - 1: # TOP ROW
                                    if prev[i][j+1] == 1:
                                        out[i][j+1] = 2
                                    if prev[i][j-1] == 1:
                                        out[i][j-1] = 2
                                    if prev[i+1][j] == 1:
                                        out[i+1][j] = 2
                                elif i < len(prev) - 1 and j == 0: # LEFT COLUMN
                                    if prev[i+1][j] == 1:
                                        out[i+1][j] = 2
                                    if prev[i-1][j] == 1:
                                        out[i-1][j] = 2
                                    if prev[i][j+1] == 1:
                                        out[i][j+1] = 2
                                elif i == len(prev) - 1 and j < len(prev[i]) - 1: # BOTTOM ROW
                                    if prev[i][j+1] == 1:
                                        out[i][j+1] = 2
                                    if prev[i][j-1] == 1:
                                        out[i][j-1] = 2
                                    if prev[i-1][j] == 1:
                                        out[i-1][j] = 2
                                elif i < len(prev) - 1 and j == len(prev[i]) - 1: # RIGHT COLUMN
                                    if prev[i+1][j] == 1:
                                        out[i+1][j] = 2
                                    if prev[i-1][j] == 1:
                                        out[i-1][j] = 2
                                    if prev[i][j-1] == 1:
                                        out[i][j-1] = 2
                                elif i < len(prev) - 1 and j < len(prev) - 1: # MIDDLE
                                    if prev[i][j+1] == 1:
                                        out[i][j+1] = 2
                                    if prev[i][j-1] == 1:
                                        out[i][j-1] = 2
                                    if prev[i-1][j] == 1:
                                        out[i-1][j] = 2
                                    if prev[i+1][j] == 1:
                                        out[i+1][j] = 2
        printGrid(out, "OUT")                
    update()
    update()

        

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))
grid = [[2,1,1],[1,1,0],[1,0,1]]
print(orangesRotting(grid))
grid = [[0,2]]
print(orangesRotting(grid))