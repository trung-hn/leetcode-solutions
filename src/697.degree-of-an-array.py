#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#

# @lc code=start
# TAGS: Array, Hash Table

import collections
from typing import List


class Solution:
    # 232 ms, 93%. Time: O(N). Space: O(N)
    def findShortestSubArray(self, nums: List[int]) -> int:
        counters = collections.Counter(nums)

        mx_freq = max(counters.values())
        mx_nums = set(num for num, freq in counters.items() if freq == mx_freq)

        first_i = {}
        last_i = {}
        for i, num in enumerate(nums):
            if num not in first_i:
                first_i[num]
            last_i[num] = i
        return min(last_i[num] - first_i[num] + 1 for num in mx_nums)

    # 256 ms, 55%. O(N). one pass
    def findShortestSubArray3(self, nums):
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
