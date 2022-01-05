# LEET CODE 198 House Robber
# You are a robber and are robbing houses for
# money, but when you rob one house you can't
# rob the house directly next it.
# Given an integer array nums representing the
# amount of money in each houyse, return the max
# amount of money you can rob in one night without
# getting caught.
def rob(nums):
    m1, m2 = 0, 0
    for n in nums:
        tmp = max(n + m1, m2)
        m1 = m2
        m2 = tmp
    return m2

test_cases = [[1,2,3,1],
              [1,5,2,8,4,3,6,2],
              [2,5,3,8,0,3],
              [12,7,5,2,9,12,15,61,2,2,2,2,2,]]
for case in test_cases:
    print(rob(case))