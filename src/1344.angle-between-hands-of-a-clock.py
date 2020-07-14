#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#

# @lc code=start
# TAGS: Math
class Solution:
    # 28 ms, 33%. Time, Space: O(1)
    def angleClock(self, hour: int, minutes: int) -> float:
        h = ((hour/12 + (minutes/60)/12) * 360 )% 360
        m = (minutes/60) * 360
        return min(abs(h-m), 360 - abs(h-m))
        
# @lc code=end

