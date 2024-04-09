#
# @lc app=leetcode id=3091 lang=python3
#
# [3091] Apply Operations to Make Sum of Array Greater Than or Equal to k
#


# @lc code=start
# TAGS: Math, Greedy, Enumeration
class Solution:
    # Time and Space: O(1). Math
    def minOperations(self, k: int) -> int:
        n = ceil(k**0.5)
        return (n - 1) + (k - 1) // n

    # Binary Search.
    # Time: O(logN). Space: O(1)
    def minOperations(self, k: int) -> int:
        def total(n):
            half = n // 2
            return (half + 1) * (n - half + 1)

        lo, hi = 0, k
        while lo < hi:
            mid = (lo + hi) // 2
            if total(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo


# @lc code=end
