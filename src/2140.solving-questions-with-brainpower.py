#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start
# TAGS: Array, Dynamic Programming
from typing import List


class Solution:
    # 3090 ms. Time and Space: O(N)
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0] * (N + 1)
        for i in reversed(range(N)):
            pts, brain = questions[i]
            total = pts
            if i + brain + 1 < N:
                total += dp[i + brain + 1]
            dp[i] = max(total, dp[i + 1])
        return dp[0]
# @lc code=end
