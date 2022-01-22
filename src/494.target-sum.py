#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
# TAGS: Dynamic Programming, DFS
# REVIEWME: Dynamic Programming, Template for DP
import collections
from typing import List
import functools


class Solution:
    # 256 ms, 68.25%. Time and Space: O(N*T). Top down approach, dfs with memoization
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @functools.cache
        def dfs(i=0, sofar=0):
            if i == len(nums):
                return sofar == target
            add = dfs(i + 1, sofar + nums[i])
            sub = dfs(i + 1, sofar - nums[i])
            return add + sub
        return dfs()

    # 3120 ms, 5.03%. Time and Space: O(N*T). Bottom Up approach
    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        dp = collections.defaultdict(int)
        dp[(0, 0)] = 1
        for i, val in enumerate(nums):
            # Try all possible sum
            for total in range(-1000, 1001):
                dp[(i + 1, total + val)] += dp[(i, total)]
                dp[(i + 1, total - val)] += dp[(i, total)]
        return dp[len(nums), target]

    # 192 ms, 84.11%. Time: O(N*T). Space: O(T) Optimized Bottom Up approach
    def findTargetSumWays3(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for num in nums:
            nxt = collections.defaultdict(int)
            # Only try sum that are in dp
            for total in dp:
                nxt[total + num] += dp[total]
                nxt[total - num] += dp[total]
            dp = nxt
        return dp[target]


# @lc code=end
