#
# @lc app=leetcode id=2139 lang=python3
#
# [2139] Minimum Moves to Reach Target Score
#

# @lc code=start
# TAGS: Math, Greedy
class Solution:
    # 48 ms, 100%. Time: O(logN). Space: O(1). Greedy
    def minMoves(self, target: int, maxDoubles: int) -> int:
        cnt = 0
        while target > 1 and maxDoubles:
            cnt += 1 + target % 2
            target //= 2
            maxDoubles -= 1
        return cnt + (target - 1)
# @lc code=end
