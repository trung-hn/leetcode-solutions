#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start
# TAGS: Math, Dynamic Programming, Backtracking


class Solution:
    # 24 ms, 93.40%. Time and Space: O(1)
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        def f(n, step=0):
            if n == 0:
                return 1
            if n == 1:
                return 9
            return f(n - 1, step + 1) * (9 - step)
        return sum(f(i) for i in range(n + 1))
# @lc code=end
