# LEET CODE 832 Flipping an Image
# given a list of 1's and 0's, flip and invert the img
# to flip, every row is reversed, and to invert is to 
# switch every 1 to 0 and 0 to 1

def printImg(i):
    for r in i:
        print(r)
    print()

def flipAndInvertImage(image):
    for r in range(len(image)):
        image[r] = image[r][::-1]
    return [[1 if image[r][c] == 0 else 0 for c in range(len(image))] for r in range(len(image))]


img = [[1,1,0],
       [1,0,1],
       [0,0,0]]
printImg(img)
printImg(flipAndInvertImage(img))

        