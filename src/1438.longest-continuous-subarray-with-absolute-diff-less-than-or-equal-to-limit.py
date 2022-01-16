#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start
# TAGS: Array, Queue, Sliding Window, Heap, Ordered Set, Monotonic Queue
# REVIEWME: Monotonic Queue
import collections
from typing import List


class Solution:
    # 732 ms, 63%. Time and Space: O(N)
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        los = collections.deque([])
        his = collections.deque([])
        left = ans = 0
        for right, num in enumerate(nums):

            # Maintain lower bound with queue
            while los and nums[los[-1]] >= num:
                los.pop()
            los.append(right)

            # Maintain upper bound with queue
            while his and nums[his[-1]] <= num:
                his.pop()
            his.append(right)

            # Sliding Window
            diff = nums[his[0]] - nums[los[0]]
            while diff > limit:
                left += 1
                if los and left > los[0]:
                    los.popleft()
                if his and left > his[0]:
                    his.popleft()
                diff = nums[his[0]] - nums[los[0]]
            ans = max(ans, right - left + 1)
        return ans
# @lc code=end
