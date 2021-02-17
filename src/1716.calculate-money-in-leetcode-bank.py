#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
#

# @lc code=start
# TAGS: Math, Greedy
class Solution:
    # 28 ms, 93.9%. Time: O(N). Space:
    def totalMoney(self, n: int) -> int:
        one_week = 28
        d, c = divmod(n, 7)
        total = 0
        for week in range(d):
            total += one_week + week * 7
        if c:
            for i in range(1, c + 1):
                total += i + d
        return total
            
# @lc code=end

