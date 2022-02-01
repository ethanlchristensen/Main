# LEET CODE 189 Rotate Array
# Given an array, rotate the array to the right by k steps
# where k is non-negative . . .

def rotate(nums, k):
    if len(nums) < 2:
        return
    if len(nums) == 2:
        if k % 2 == 0:
            return
        else:
            tmp = nums[0]
            nums[0] = nums[1]
            nums[1] = tmp
            return
    tmp = nums[k+1:] + nums[:k+1]
    print(len(tmp))
    for i in range(len(nums)):
        nums[i] = tmp[i]
    return

n = [1,2]
rotate(n,2)
print(n)
rotate(n,1)
print(n)
n = [1,2,3,4,5,6,7]
rotate(n,3)
print(n)
n = [-1,-100,3,99]
rotate(n,2)
print(n)
