def mergeSorted(nums1, m, nums2, n):
    last = m + n - 1

    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n-= 1
        last -= 1

    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        m -= 1


n1 = [1,2,5,6,10,0,0,0]
n1l = 5
n2 = [2,5,8]
n2l = 3
mergeSorted(n1, n1l, n2, n2l)
print(n1)