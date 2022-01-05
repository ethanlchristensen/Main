# LEET CODE 994 Rotting Oranges
# Given an array of 0's, 1's, and 2's where
# 0 = empty space
# 1 = fresh orange
# 2 = rotten orange
# Determine the amount of time it will take for every orange to become
# rotten given that oranges become rotten if there non-diagonal neighbor
# is rotten. Return the number of minutes passed in order for all oranges
# to become rotten, or -1 if it is not possible.
def printGrid(l):
    if len(l[0]) % 2 == 0:
        print("="*(len(l[0]) * 2 +4))
    else:
        print("="*(len(l[0]) * 2 + 5))
    for r in l:
        print("  ", end="")
        for c in r:
            if c == 2:
                print('R', end="  ")
            elif c == 1:
                print('F', end="  ")
            else:
                print('#', end="  ")
        print()
    if len(l[0]) % 2 == 0:
        print("="*(len(l[0]) * 2 + 4))
    else:
        print("="*(len(l[0]) * 2 + 5))

def orangesRotting(grid):
    MINUTES = 0
    FRESH = 1
    ROTTEN = 2
    M = len(grid)
    N = len(grid[0])

    def helperMain(g):
        new = [[-1 for c in range(N)] for r in range(M)]
        for r in range(M):
            for c in range(N):
                if g[r][c] == ROTTEN:
                    if r == 0 and c == 0:
                        if g[r][c+1] == FRESH:
                            new[r][c+1] = ROTTEN
                        if g[r+1][c] == FRESH:
                            new[r+1][c] = ROTTEN
                    elif r == 0 and c == N-1:
                        if g[r][c-1] == FRESH:
                            new[r][c-1] = ROTTEN
                        if g[r+1][c] == FRESH:
                            new[r+1][c] = ROTTEN
                    elif r == M-1 and c == 0:
                        if g[r][c+1] == FRESH:
                            new[r][c+1] = ROTTEN
                        if g[r-1][c] == FRESH:
                            new[r-1][c] = ROTTEN
                    elif r == M-1 and c == N-1:
                        if g[r][c-1] == FRESH:
                            new[r][c-1] = ROTTEN
                        if g[r-1][c] == FRESH:
                            new[r-1][c] = ROTTEN
                    elif r == 0 and c < N-1:
                        if g[r][c-1] == FRESH:
                            new[r][c-1] = ROTTEN
                        if g[r][c+1] == FRESH:
                            new[r][c+1] = ROTTEN
                        if g[r+1][c] == FRESH:
                            new[r+1][c] = ROTTEN
                    elif r == M-1 and c < N-1:
                        if g[r][c-1] == FRESH:
                            new[r][c-1] = ROTTEN
                        if g[r][c+1] == FRESH:
                            new[r][c+1] = ROTTEN
                        if g[r-1][c] == FRESH:
                            new[r-1][c] = ROTTEN
                    elif r < M-1 and c == 0:
                        if g[r-1][c] == FRESH:
                            new[r-1][c] = ROTTEN
                        if g[r+1][c] == FRESH:
                            new[r+1][c] = ROTTEN
                        if g[r][c+1] == FRESH:
                            new[r][c+1] = ROTTEN
                    elif r < M-1 and c == N-1:
                        if g[r-1][c] == FRESH:
                            new[r-1][c] = ROTTEN
                        if g[r+1][c] == FRESH:
                            new[r+1][c] = ROTTEN
                        if g[r][c-1] == FRESH:
                            new[r][c-1] = ROTTEN
                    elif r < M-1 and c < N-1:
                        if g[r][c-1] == FRESH:
                            new[r][c-1] = ROTTEN
                        if g[r][c+1] == FRESH:
                            new[r][c+1] = ROTTEN
                        if g[r-1][c] == FRESH:
                            new[r-1][c] = ROTTEN
                        if g[r+1][c] == FRESH:
                            new[r+1][c] = ROTTEN
                if new[r][c] != ROTTEN:
                    new[r][c] = g[r][c]
        return (g, new)

        
    def helperSmall(g):
        new = [[-1 for c in range(N)] for r in range(M)]
        if M < 2 and N < 2:
            new[M-1][N-1] = g[M-1][N-1]
            return (g, new)
        elif M < 2 and N >= 2:
            for c in range(N-1):
                if g[M-1][c] == ROTTEN:
                    if c == 0:
                        if g[M-1][c+1] == FRESH:
                            new[M-1][c+1] = ROTTEN
                    else:
                        if g[M-1][c-1] == FRESH and g[M-1][c+1] == FRESH:
                            new[M-1][c-1] = ROTTEN
                            new[M-1][c+1] = ROTTEN
                        elif g[M-1][c-1] == FRESH:
                            new[M-1][c-1] = ROTTEN
                        elif g[M-1][c+1] == FRESH:
                            new[M-1][c+1] = ROTTEN
                if new[M-1][c] != ROTTEN:
                    new[M-1][c] = g[M-1][c]
            if new[M-1][N-1] != ROTTEN:
                new[M-1][N-1] = g[M-1][N-1]
            if new[M-1][N-1] == ROTTEN and new[M-1][N-2] == FRESH:
                new[M-1][N-2] = ROTTEN
            return (g, new)
        elif M >= 2 and N < 2:
            for r in range(M-1):
                if g[r][N-1] == ROTTEN:
                    if r == 0:
                        if g[r+1][N-1] == FRESH:
                            new[r+1][N-1] = ROTTEN
                    else:
                        if g[r-1][N-1] == FRESH and g[r+1][N-1] == FRESH:
                            new[r-1][N-1] = ROTTEN
                            new[r+1][N-1] = ROTTEN
                        elif g[r-1][N-1] == FRESH:
                            new[r-1][N-1] = ROTTEN
                        elif g[r+1][N-1] == FRESH:
                            new[r+1][N-1] = ROTTEN
                if new[r][N-1] != ROTTEN:
                    new[r][N-1] = g[r][N-1]
            if new[M-1][N-1] != ROTTEN:
                new[M-1][N-1] = g[M-1][N-1]
            if new[M-1][N-1] == ROTTEN and new[M-2][N-1] == FRESH:
                new[M-2][N-1] = ROTTEN
            return (g, new)
    if M == 0 and N == 0:
        return -1
    if M >= 2 and N >= 2:
        o, n = helperMain(grid)
        printGrid(o)
        while o != n:
            printGrid(n)
            MINUTES += 1
            o, n = helperMain(n)
        for r in n:
            if 1 in r:
                return -1
        return MINUTES
    else:
        o, n = helperSmall(grid)
        while o != n:
            MINUTES += 1
            o, n = helperSmall(n)
        for r in n:
            if 1 in r:
                return -1
        return MINUTES
    


orangeGrid = [[2,1,1],
              [1,1,0],
              [0,1,1]]
print(orangesRotting(orangeGrid))
orangeGrid = [[2,1],
              [1,1]]
print(orangesRotting(orangeGrid))
orangeGrid = [[2,1,1,1,2,1,0]]
print(orangesRotting(orangeGrid))
orangeGrid = [[2],
              [1],
              [1],
              [1],
              [2],
              [1],
              [0],
              [1]]
print(orangesRotting(orangeGrid))
orangeGrid = [[1,2]]
print(orangesRotting(orangeGrid))
orangeGrid = [[1],
              [2],
              [0],
              [0],
              [1],
              [2],
              [0]]
print(orangesRotting(orangeGrid))