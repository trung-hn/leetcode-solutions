#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
# TAGS: Array, Hash Table

import collections
from typing import List

# 1. Find degree of the array
# 2. Find elements with degree
# 3. Find leftmost and rightmost index of the elements from step 2
# 4. Find minimum (right - left) + 1


class Solution:
    # 360 ms, 46%. Time: O(N). Space: O(N)
    def findShortestSubArray(self, nums: List[int]) -> int:
        counters = collections.Counter(nums)

        degree = max(counters.values())
        elements = [num for num, freq in counters.items() if freq == degree]

        first_i = {}
        last_i = {}
        for i, num in enumerate(nums):
            if num not in first_i:
                first_i[num] = i
            last_i[num] = i
        return min(last_i[num] - first_i[num] + 1 for num in elements)

    # 321 ms, 57%. O(N).
    # Only go through nums once instead of multiple times like previous solution
    def findShortestSubArray2(self, nums):
        first, count, ans, degree = {}, {}, 0, 0
        for i, num in enumerate(nums):
            first.setdefault(num, i)
            count[num] = count.get(num, 0) + 1
            if count[num] > degree:
                degree = count[num]
                ans = i - first[num] + 1
            elif count[num] == degree:
                ans = min(ans, i - first[num] + 1)
        return ans


# @lc code=end
