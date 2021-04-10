#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
# TAGS: Dynamic Programming, DFS
# REVIEWME: Dynamic Programming, Template for DP
import collections


class Solution:
    # 256 ms, 68.25%. Time and Space: O(N*T). Top down approach, dfs with memo
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i=0, sofar=0):
            if i == len(nums):
                return sofar == target
            add = dfs(i + 1, sofar + nums[i])
            sub = dfs(i + 1, sofar - nums[i])
            return add + sub
        return dfs()

    # 3120 ms, 5.03%. Time and Space: O(N*T). Bottom Up approach.
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = collections.defaultdict(int)
        dp[(0, 0)] = 1
        for i, val in enumerate(nums, 1):
            # Try all possible sum
            for sm in range(-1000, 1001):
                dp[(i, sm + val)] += dp[(i - 1, sm)]
                dp[(i, sm - val)] += dp[(i - 1, sm)]
        return dp[len(nums), target]

    # 192 ms, 84.11%. Time: O(N*T). Space: O(T) Bottom up approach with optimized space
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for i, val in enumerate(nums):
            nxt = collections.defaultdict(int)
            # Only try sum that are in dp
            for sofar in dp:
                nxt[sofar + val] += dp[sofar]
                nxt[sofar - val] += dp[sofar]
            dp = nxt
        return dp[target]


# @lc code=end
