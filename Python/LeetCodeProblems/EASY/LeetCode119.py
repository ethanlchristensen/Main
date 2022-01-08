# LEET CODE 119 Pascal's Triangle 2
# given an index, return the row in Pascal's Triangle at row index


def getRow(rowIndex):
    res = []
    for i in range(1, rowIndex + 2): 
        res.append([res[i-2][j-1]+res[i-2][j] if 0 < j < i-1 else 1 for j in range(i)])
    return res[-1]

print(getRow(0))

