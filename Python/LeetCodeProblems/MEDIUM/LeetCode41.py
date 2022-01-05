# LEET CODE 41 FIRST MISSING POSITIVE
# Given a list of numbers, return the first missing
# positive number in the array. For example . . . 
# [1, 2, 0] -> 3
# [3, 4, -1, 1] -> 2
# [7, 8, 9, 11, 12] -> 1

def first_missing_positive(nums):
    nums = set(nums)
    i = 1
    while i in nums:
        i += 1
    return i

test_cases = [[1, 2, 0], 
              [3, 4, -1, 1], 
              [7, 8, 9, 11, 12]]

for case in test_cases:
    print(first_missing_positive(case))