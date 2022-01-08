# Leet Code 118 Pascal's Triangle
# Given an int for num of rows, generate numRows
# of Pascal's Triangle.
#                  1
#                1   1
#              1   2   1
#            1   3   3   1
def printTriangle(triangle):
    for r in triangle:
        print(r)
    print()


def generate(numRows):
    res = []
    for i in range(1, numRows + 1): 
        res.append([res[i-2][j-1]+res[i-2][j] if 0 < j < i-1 else 1 for j in range(i)])
    return res


def generateExpanded(numRows):
    res = []
    for i in range(1, numRows + 1):
        tmp = []
        for j in range(i):
            if 0 < j < i-1:
                tmp.append(res[i-2][j-1] + res[i-2][j])
            else:
                tmp.append(1)
        res.append(tmp)
    return res


printTriangle(generate(3))