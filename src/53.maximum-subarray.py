#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
# TAGS: Pythonic, Dynamic Programming
# REVIEWME:
from itertools import accumulate
class Solution:
    # Pythonic
    def maxSubArray(self, nums: List[int]) -> int:
        return max(accumulate(nums, lambda x, y: max(y, x+y) ))
    
    def maxSubArray(self, nums: List[int]) -> int:
        max_sofar = max_cur =  float('-inf')
        for num in nums:
            max_cur = max(max_cur + num, num)
            max_sofar = max(max_sofar, max_cur)
        return max_sofar

    # 64 ms, 81.72%
    def maxSubArray(self, nums: List[int]) -> int:
        max_sofar = max_cur = float("-inf")
        for num in nums:
            max_cur += num
            if max_cur < num:
                max_cur = num
            max_sofar = max(max_cur, max_sofar)
        return max_sofar
# @lc code=end

