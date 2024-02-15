#
# @lc app=leetcode id=2971 lang=python3
#
# [2971] Find Polygon With the Largest Perimeter
#

# @lc code=start
# TAGS: Array, Greedy, Sorting, Prefix Sum

import heapq
from typing import List


class Solution:
    # Time: O(NlogN). Space: O(N)
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = sum(nums)
        while nums:
            num = nums.pop()
            if num < total / 2 and len(nums) > 1:
                return total
            total -= num
        return -1

    # Time and Space: O(N).
    # Time O(N) because there is a limit to sum(A)
    def largestPerimeter(self, A: List[int]) -> int:
        cur = sum(A)
        heapq._heapify_max(A)
        while A and cur <= A[0] * 2:
            cur -= heapq._heappop_max(A)
        return cur if len(A) > 2 else -1


# @lc code=end
