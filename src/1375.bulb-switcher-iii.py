#
# @lc app=leetcode id=1375 lang=python3
#
# [1375] Bulb Switcher III
#

# @lc code=start
# TAGS: Array
class Solution:
    # 432 ms, 90%. O(N), O(1). Optimal
    def numTimesAllBlue(self, light: List[int]) -> int:
        high_bulb = blue_state_cnt = 0
        for i, bulb in enumerate(light, 1):
            high_bulb = max(high_bulb, bulb)
            if high_bulb == i: blue_state_cnt += 1
        return blue_state_cnt


# @lc code=end

