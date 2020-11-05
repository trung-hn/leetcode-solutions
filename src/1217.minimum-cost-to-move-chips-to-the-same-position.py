#
# @lc app=leetcode id=1217 lang=python3
#
# [1217] Minimum Cost to Move Chips to The Same Position
#

# @lc code=start
# TAGS: Array, Greedy. Math
class Solution:
    # Time: O(N). Space: O(1)
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt = [0, 0]
        for chip in position:
            cnt[chip % 2] += 1
        return min(cnt)
# @lc code=end

