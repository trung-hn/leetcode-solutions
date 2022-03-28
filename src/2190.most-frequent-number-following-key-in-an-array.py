#
# @lc app=leetcode id=2190 lang=python3
#
# [2190] Most Frequent Number Following Key In an Array
#

# @lc code=start
# TAGS: Array, Hash Table, Counting
from typing import List
import collections


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt = collections.Counter()
        for v1, v2 in zip(nums, nums[1:]):
            if v1 == key:
                cnt[v2] += 1
        return max(cnt, key=lambda x: cnt.get(x))
# @lc code=end
