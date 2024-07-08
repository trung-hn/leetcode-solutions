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

    # Time: O(N^3). Space: O(1)
    def countSubarrays1(self, nums: List[int], k: int) -> int:
        ans = 0
        mx = max(nums)
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                if nums[left : right + 1].count(mx) >= k:
                    ans += 1
        return ans

    # Time: O(N^2). Space: O(1)
    def countSubarrays2(self, nums: List[int], k: int) -> int:
        ans = 0
        mx = max(nums)
        for left in range(len(nums)):
            cnt = 0
            for right in range(left, len(nums)):
                cnt += nums[right] == mx
                ans += cnt >= k
        return ans

    # Time and Space: O(N).
    def countSubarrays3(self, nums: List[int], k: int) -> int:
        ans = left = 0
        mx = max(nums)
        counter = collections.Counter()
        for _, num in enumerate(nums):  # right
            counter[num] += 1
            while counter[mx] > k or nums[left] != mx:  # left
                counter[nums[left]] -= 1
                left += 1
            if counter[mx] >= k:
                ans += left + 1
        return ans


# @lc code=end
