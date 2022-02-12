#
# @lc app=leetcode id=1991 lang=python3
#
# [1991] Find the Middle Index in Array
#

# @lc code=start
from typing import List


class Solution:
    # Time and Space: O(N)
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix_sum = [0]
        for val in nums:
            prefix_sum.append(prefix_sum[-1] + val)

        for i in range(1, len(prefix_sum)):
            left = prefix_sum[i - 1] - prefix_sum[0]
            right = prefix_sum[-1] - prefix_sum[i]
            if left == right:
                return i - 1
        return -1
# @lc code=end
