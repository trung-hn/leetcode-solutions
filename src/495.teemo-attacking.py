#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#

# @lc code=start
# TAGS: Array
class Solution:
    # 248 ms, 99.52%. Time: O(N). Space: O(1)
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries: return 0
        total = 0
        for t1, t2 in zip(timeSeries, timeSeries[1:]):
            total += min(duration, t2 - t1)
        return total + duration

# @lc code=end

