#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
import collections
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if num in D:
                return [D[num], i]
            D[target - num] = i



