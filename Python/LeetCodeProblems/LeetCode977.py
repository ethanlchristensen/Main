# LEET CODE 997 SQUARES OF A SORTED ARRAY
# Given a sorted array of integers, return
# an array of the elements squared this is
# also sorted. Squaring all elements and then
# sorting is trivial and is O( n log n ). . .
# can you find a O( n ) solution? 
import math

def sortedSquares(nums):
    l = 0
    r = len(nums) - 1
    while l != r:
        if abs(nums[l]) >= abs(nums[r]):
            tmp = nums[r]
            nums[r] = nums[l] ** 2
            nums[l] = tmp
            r -= 1
        else:
            nums[r] = nums[r] ** 2
            r -= 1
    nums[l] = nums[l] ** 2
    return nums
        

test_cases = [[-4, -1, 0, 3, 10], [-5,-3,-2,-1]]

for case in test_cases:
    print(sortedSquares(case))
