#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
# TAGS: Array


class Solution:
    # 36 ms, 57.22%. Time: O(N). Space: O(1)
    def largestAltitude(self, gain: List[int]) -> int:
        running_sum = result = 0
        for g in gain:
            running_sum += g
            result = max(result, running_sum)
        return result
# @lc code=end
