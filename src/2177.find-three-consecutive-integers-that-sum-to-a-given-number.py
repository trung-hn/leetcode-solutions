#
# @lc app=leetcode id=2177 lang=python3
#
# [2177] Find Three Consecutive Integers That Sum to a Given Number
#

# @lc code=start
# TAGS: Math, Binary Search
from typing import List


class Solution:
    # 36 ms, 79.85 %. Time: O(logN). Space: O(1). Binary Search
    def sumOfThree(self, num: int) -> List[int]:
        lo = -1
        hi = 10 ** 15
        while lo < hi:
            mid = (lo + hi) // 2
            total = mid * 3 + 3
            if total >= num:
                hi = mid
            else:
                lo = mid + 1
        if lo * 3 + 3 == num:
            return range(lo, lo + 3)
        return []

    # Time and Space: O(1). Math
    def sumOfThree(self, num: int) -> List[int]:
        div = (num - 3) / 3
        if div == int(div):
            div = int(div)
            return range(div, div + 3)
        return []
# @lc code=end
