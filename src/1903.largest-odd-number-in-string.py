#
# @lc app=leetcode id=1903 lang=python3
#
# [1903] Largest Odd Number in String
#

# @lc code=start
# TAGS: Math, String, Greedy


class Solution:
    # 52 ms, 61.71%. Time: O(N). Space: O(1)
    def largestOddNumber(self, num: str) -> str:
        for i in reversed(range(len(num))):
            if int(num[i]) % 2:
                return num[: i + 1]
        return ''
# @lc code=end
