#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
import collections
class Solution:
    # HashMap, Dictionary
    # Time: O(N)
    # Space: O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        D = collections.defaultdict(int)
        for i, num in enumerate(nums):
            if target - num in D:
                return [D[num], i]
            D[num] = i


    # Bruteforce
    # TimeComplexity = O(N^2)
    # Space Complexity = O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): 
                if nums[i] + nums[j] == target:
                    return [i, j]
