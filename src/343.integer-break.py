#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#


# @lc code=start
# TAGS: Math, Dynamic Programming
class Solution:
    # 28 ms, 95.47%
    # Time: O(N). Space: O(1)
    def integerBreak(self, n: int) -> int:
        """Just Math"""
        ans = 0
        for k in range(2, n + 1):
            d, left_over = divmod(n, k)
            ans = max(ans, d ** (k - left_over) * (d + 1) ** left_over)
        return ans


# @lc code=end
