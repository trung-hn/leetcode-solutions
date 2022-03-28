#
# @lc app=leetcode id=2191 lang=python3
#
# [2191] Sort the Jumbled Numbers
#

# @lc code=start
# TAGS: Array, Sorting
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping = {str(i): str(v) for i, v in enumerate(mapping)}

        def custom_key(num):
            new = []
            for d in str(num):
                new.append(mapping[d])
            return int("".join(new))
        return sorted(nums, key=custom_key)
# @lc code=end
