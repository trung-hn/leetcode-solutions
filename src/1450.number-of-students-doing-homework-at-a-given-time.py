#
# @lc app=leetcode id=1450 lang=python3
#
# [1450] Number of Students Doing Homework at a Given Time
#

# @lc code=start
class Solution:
    """
    64 ms, 35.27%. Time: O(N). Space: O(1)
    """
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(lo <= queryTime <= hi for lo, hi in zip(startTime, endTime))
# @lc code=end

