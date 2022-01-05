# LEET CODE 35 Search Insert Position
# given an list sorted, and a target value
# find the index where target is, or the index
# where target should go if it is not in the list

def searchInsert(nums, target):
    if nums[len(nums)-1] < target:
        return len(nums)
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if nums[i] > target:
            return i

test_cases = [[1,3,5,6],5,[1,3,5,6],2,[1,3,5,6],7]
for i in range(0,len(test_cases),2):
    print("{} --> {} --> INDEX: {}".format(test_cases[i+1],test_cases[i],searchInsert(test_cases[i],test_cases[i+1])))
