#
# @lc app=leetcode id=1736 lang=python3
#
# [1736] Latest Time by Replacing Hidden Digits
#

# @lc code=start
# TAGS: String, Greedy


class Solution:
    # 28 ms, 83.11%. Time and Space: O(1)
    def maximumTime(self, time: str) -> str:
        first, second, _, third, fourth = time

        if first == second == "?":
            first, second = "23"
        elif first == "?":
            first = "2" if second in "0123" else "1"
        elif second == "?":
            second = "9" if first in "01" else "3"

        if third == "?":
            third = "5"
        if fourth == "?":
            fourth = "9"

        return first + second + ":" + third + fourth
# @lc code=end
