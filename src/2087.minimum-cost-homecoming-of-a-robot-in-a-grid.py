#
# @lc app=leetcode id=2087 lang=python3
#
# [2087] Minimum Cost Homecoming of a Robot in a Grid
#

# @lc code=start
# TAGS: Array, Greedy, Matrix
from typing import List


class Solution:
    # 2165 ms, 9.33%. Time: O(N). Space: O(1)
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        r0, c0 = startPos
        r1, c1 = homePos
        ans = 0
        ans += sum(rowCosts[r0 + 1: r1 + 1] if r0 < r1 else rowCosts[r1: r0])
        ans += sum(colCosts[c0 + 1: c1 + 1] if c0 < c1 else colCosts[c1: c0])
        return ans
# @lc code=end
