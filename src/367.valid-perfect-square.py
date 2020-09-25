#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
# TAGS: Math, Binary Search
class Solution:
    # O(N)
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0: return 0
        d = 1
        while d**2 < num:
            d += 1
        return d**2 == num
    # 28 ms, 75.96%. O(log N). Space: O(1)
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0: return 0
        lo, hi = 1, num //2
        while lo < hi:
            mid = (lo + hi) // 2
            if mid**2 >= num:
                hi = mid
            else:
                lo = mid + 1
        return lo ** 2 == num
        
# @lc code=end
