import copy

def printGrid(inGrid, name):
    print("GRID:", name)
    for i in inGrid:
        print(i)



def orangesRotting(grid):
    print("CARSON IS COOL")

        

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))
grid = [[2,1,1],[1,1,0],[1,0,1]]
print(orangesRotting(grid))
grid = [[0,2]]
print(orangesRotting(grid))