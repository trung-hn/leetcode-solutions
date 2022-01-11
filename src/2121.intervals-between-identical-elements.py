#
# @lc app=leetcode id=2121 lang=python3
#
# [2121] Intervals Between Identical Elements
#

# @lc code=start
# TAGS: Array, Hash Table, Prefix Sum
import collections
from typing import List


class Solution:
    # 1300 ms, 89.94%. Time and Space: O(N)
    def getDistances(self, arr: List[int]) -> List[int]:

        def get_init_dist(nums):
            val = nums[0]
            return sum(num - val for num in nums[1:])

        # Group indices by its value
        seen = collections.defaultdict(list)
        for i, val in enumerate(arr):
            seen[val].append(i)

        # DP
        dp = [0] * len(arr)
        for values in seen.values():
            dp[values[0]] = get_init_dist(values)
            for i in range(1, len(values)):
                v1, v2 = values[i - 1: i + 1]
                diff = v2 - v1
                dp[v2] = dp[v1] + diff * (2 * i - len(values))
        return dp


# @lc code=end
