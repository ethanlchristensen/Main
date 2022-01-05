# LEET CODE 26 Remove Duplicates From Sorted List
# Given a List sorted in non-decreasing order, remove the duplicate
# in place such that each unique element appears only once. The realtive
# order of the elements should be kept the same.

def removeDuplicates(nums):
    if nums == []:
        return 0
    k = 1;
    prev = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != prev:
            nums[k] = nums[i]
            prev = nums[i]
            k += 1
    return k

test_cases = [[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8],
              [1,1,1,1,2,3,3,4,4,5,6,7,7,8],
              [1,2,3,4,5,6,7,8,9,9,9,9],
              [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,7,8,9,9],
              [1,1,1,1,2,2,3,3,4,4,5,6,7,7,8,9,9,10]]

for i in range(len(test_cases)):
    print("LIST:", i)
    for j in range(len(test_cases[i])):
        print(test_cases[i][j], end=" ")
    print()

updated = {}
for i in range(len(test_cases)):
    updated[i] = [removeDuplicates(test_cases[i]), test_cases[i]]
for group in updated:
    print("UPDATED LIST: GROUP:", group)
    for i in range(updated[group][0]):
        print(updated[group][1][i], end=" ")
    print()
