#
# @lc app=leetcode id=2136 lang=python3
#
# [2136] Earliest Possible Day of Full Bloom
#

# @lc code=start
# TAGS: Array, Greedy, Sorting
from typing import List


class Solution:
    # Observation:
    # - There is no point in plating in non-consecutive days
    # - plant the one that takes most day to grow first.
    # Time: O(Sort). Space: O(Sort)
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plants = sorted(zip(growTime, plantTime), reverse=True)
        cur = cur_max = 0
        for g, p in plants:
            cur_max = max(cur_max, cur + p + g)
            cur += p
        return cur_max


# @lc code=end
