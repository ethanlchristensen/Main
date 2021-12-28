# LEET CODE 997 SQUARES OF A SORTED ARRAY
# Given a sorted array of integers, return
# an array of the elements squared this is
# also sorted. Squaring all elements and then
# sorting is trivial and is O( n log n ). . .
# can you find a O( n ) solution? 

def sortedSquares(nums):
    p = len(nums) - 1 # right most pointer
    while p != -1:
        if nums[0] ** 2 >= nums[p] ** 2:
            tmp = nums[p]
            nums[p] = nums[0] ** 2
            nums[0] = tmp
            p -= 1
        else:
            nums[p] = nums[p] ** 2
            p -= 1
    nums[0] = nums[0] ** 2
    return nums

l = [-5, -3, -2, -1]
print(sortedSquares(l))