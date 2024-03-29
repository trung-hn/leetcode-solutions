#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#


# @lc code=start
# TAGS: Array, Hash Table, Sliding Window
import collections
from typing import List


class Solution:
    # Time and Space: O(N)
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = index = 0
        counter = collections.defaultdict(int)
        for i, num in enumerate(nums):
            counter[num] += 1
            while counter[num] > k:
                counter[nums[index]] -= 1
                index += 1
            ans = max(ans, i - index + 1)
        return ans


# @lc code=end
