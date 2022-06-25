#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
# TAGS: Array, DP
from typing import List


class Solution:

    # Recursive with Memoization
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(i):
            if i < 0:
                return 0
            return min(dfs(i - 1), dfs(i - 2)) + cost[i]

        N = len(cost)
        return min(dfs(N - 1), dfs(N - 2))

    # 56 ms, 75.34%. Time: O(N). Space: O(1)
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 2], cost[i - 1])
        return min(cost[-2:])


# @lc code=end
