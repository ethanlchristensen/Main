# LEET CODE 312 Burst Ballons
# Given an array of ballons with a coin value painted on them
# stored in a list, if you burts a balloon at nums[i] then you get
# nums[i-1]+nums[i]+nums[i+1] coins. If i falls out of bound add one.
# Determine the maximum number of coins you can get through carefull
# ballon bursting.

def maxCoins(nums):
    nums = [1] + nums + [1]
    dp = {}

    def dfs(l, r):
        if l > r:
            return 0
        if (l, r) in dp:
            return dp[(l,r)]
        dp[(l,r)] = 0
        for i in range(l,r+1):
            coins = nums[l-1] * nums[i] * nums[r+1]
            coins += dfs(l, i - 1) + dfs(i + 1, r)
            dp[(l,r)] = max(dp[(l,r)], coins)
        return dp[(l,r)]
    return dfs(1, len(nums) - 2)


balloons = [3,1,5,8]
print(maxCoins(balloons))
