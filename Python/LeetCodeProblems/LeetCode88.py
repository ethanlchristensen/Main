# LEET CODE 88 Merge Sorted Array
# Given two arrays, num1 and nums 2 merge the
# arrays in sorted order, but do so by modify
# the nums1 array which has space for all the 
# elements. Also you are given the size of 
# nums1 and nums2 as m and n . . For example
# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# result: nums1 = [1,2,2,3,5,6]

def merge(nums1, m, nums2, n):
    last = m + n - 1
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1


n1 = [1,2,3,0,0,0]
n2 = [2,5,6]
merge(n1, 3, n2, 3)
print(n1)