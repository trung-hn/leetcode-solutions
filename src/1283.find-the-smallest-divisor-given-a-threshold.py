#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#

# @lc code=start
# TAGS: Binary Search
from math import ceil
from typing import List


class Solution:
    # Time: O(NlogM). Space: O(1). N is len(nums), M is max(nums)
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def get_sum(div):
            return sum(ceil(val / div) for val in nums)

        lo, hi = 1, 10 ** 6
        while lo < hi:
            mid = (lo + hi) // 2
            if get_sum(mid) > threshold:
                lo = mid + 1
            else:
                hi = mid
        return lo


# @lc code=end
