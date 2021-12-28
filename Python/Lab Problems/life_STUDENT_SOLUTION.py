# Conway's Game of Life lab

# numpy (NumPy) is a library of functions that allow for easy
# generation of 2-D arrays of values, esp. random numbers.
# matplotlib.pyplot has already been discussed previously.
# matplotlib.animation enables animations on a matplotlib canvas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# setting up the values for the grid
ALIVE = 1
DEAD = 0

def randomGrid(N):
    """ this function generates an NxN list of random values """
    return np.random.choice([ALIVE,DEAD], N*N, ).reshape(N, N)

def update(frameNum, img, current, N,):
    """ this function is called automatically for animation and is
        where the work of generating the next generation happens """

    # This line makes a newGrid 2-D list for you to work in. It creates
    # a copy of the current generation, primarily to create an exact NxN
    # space to put the new generation into.
    next_gen = current.copy()

    # now, go through all rows and columns and count the number of
    # neighbors for the cell at current[r][c].
    
    for r in range(N):         # r is the current row
        for c in range(N):     # c is the current column
            # compute 8-neighbor sum, initialize total to 0 each time
            total = 0
            
            # find the stuff in the middle section (8 neighbors)
            # think about the constraints for r and c to identify only
            # cells that are in the middle section. remember that N is
            # the size of the array, so N-1 would be the bottom row and
            # the right column
            if r > 0 and r < N-1 and c > 0 and c < N-1:
                total = (current[r-1][c-1] + current[r+1][c-1] + current[r-1][c+1] + current[r+1][c+1] + current[r-1][c] + current[r+1][c] + current[r][c-1] + current[r][c+1])

            # middle top row (5 neighbors)
            elif r == 0 and c > 0 and c < N-1:
                total = (current[r][c-1] + current[r][c+1] + current[r+1][c-1] + current[r+1][c] + current[r+1][c+1])
                

            # middle bottom row (5 neighbors)
            
            elif r == N-1 and c > 0 and c < N-1:
                total = (current[r][c-1] + current[r][c+1] + current[r-1][c-1] + current[r-1][c] + current[r-1][c+1])
            
            # middle left column (5 neighbors)
            
            elif c == 0 and r > 0 and r < N-1:
                total = (current[r-1][c] + current[r+1][c] + current[r-1][c+1] + current[r][c+1] + current[r+1][c+1])

            # middle right column (5 neighbors)
            elif c == N-1 and r > 0 and r < N-1:
                total = (current[r-1][c] + current[r+1][c] + current[r-1][c-1] + current[r][c-1] + current[r+1][c-1])
            # upper left corner (3 neighbors)
            elif r == 0 and c == 0:
                total = (current[r+1][c] + current[r+1][c+1] + current[r][c+1])
            # upper right corner (3 neighbors)
            elif r == 0 and c == N-1:
                total = (current[r][c-1] + current[r+1][c-1] + current[r+1][c])
            # lower left corner (3 neighbors)
            elif r == N-1 and c == 0:
                total = (current[r][c+1] + current[r-1][c+1] + current[r-1][c])
            # lower right corner (3 neighbors)
            elif r == N-1 and c == N-1:
                total = (current[r][c-1] + current[r-1][c-1] + current[r-1][c])



            # apply Conway's rules for death and birth. you can simplify
            # the rules down to what kills a cell (loneliness or
            # overcrowding) and what causes a cell to come alive. an
            # if/else structure should be enough. make sure to write your
            # assignment statement for next_gen[r][c] to be either DEAD
            # or ALIVE
            if current[r][c] == ALIVE:
                if total < 2 or total > 3:
                    next_gen[r][c] = DEAD
            elif current[r][c] == DEAD:
                if total == 3:
                    next_gen[r][c] = ALIVE


    # update the "image" for the next animation frame. you don't need to
    # change anything here
    
    img.set_data(next_gen)
    current[:] = next_gen[:]
    return img,

# main() function. everything below here does not need to be changed, but
# could be interesting to look at in the future.

def main():
    # set grid size to at least 10 but no more than 200
    N = 0
    while N < 10 or N > 200:
        N = int(input("Enter grid size (10-200): "))

    # set animation update interval. set it to at least 10 (fastest) to
    # no more than 200 (pretty slow)
    updateInterval = 0
    while updateInterval < 5 or updateInterval > 200:
        updateInterval = int(input("Enter update speed in ms (10-200): "))

    # create a grid using numpy (np) and then fill it with random data
    grid = np.array([])
    grid = randomGrid(N)

    # set up the animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, ),
                                frames = 10,
                                interval=updateInterval,
                                save_count=50)
    plt.show()
    
# call main
if __name__ == '__main__':
    main()