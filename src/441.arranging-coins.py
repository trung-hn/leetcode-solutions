#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
# TAGS: Math, Binary Search


class Solution:
    # 36 ms, 82.51%. Time: O(logN). Space: O(1)
    def arrangeCoins(self, n: int) -> int:

        def total(i):
            return (1 + i) * (i / 2)

        left, right = 1, 2**31 - 1
        while left < right:
            mid = (left + right) // 2
            left_over = n - total(mid)
            if left_over >= mid + 1:
                left = mid + 1
            else:
                right = mid
        return left

    # 20 ms, 99.84%. Time and Space: O(1)
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
# @lc code=end
