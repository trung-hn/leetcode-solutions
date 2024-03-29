#
# @lc app=leetcode id=2962 lang=python3
#
# [2962] Count Subarrays Where Max Element Appears at Least K Times
#


# @lc code=start
# TAGS: Array, Sliding Window
import collections
from typing import List


class Solution:
    # Time and Space:O(N)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = index = 0
        mx = max(nums)
        counter = collections.Counter()
        for i, num in enumerate(nums):
            counter[num] += 1
            while counter[mx] > k or nums[index] != mx:
                counter[nums[index]] -= 1
                index += 1
            if counter[mx] < k:
                continue
            ans += index + 1
        return ans


# @lc code=end
