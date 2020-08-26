#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
# TAGS: Math
class Solution:
    # 32 ms, 66.46 %. Time and Space: O(1)
    def countOdds(self, low: int, high: int) -> int:
        low_no = low // 2
        high_no = high // 2 + high % 2
        return high_no - low_no
# @lc code=end

