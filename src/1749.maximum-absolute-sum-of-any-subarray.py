#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#

# @lc code=start
# TAGS: Greedy
class Solution:
    # 480 ms, 76.89%. Time: O(N). Space: O(N)
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        def max_subarray(arr):
            ans = float("-inf")
            total = 0
            for val in arr:
                if total < 0:
                    total = 0
                total += val
                ans = max(ans, total)
            return ans
        
        val1 = max_subarray(nums)
        val2 = max_subarray(list(-n for n in nums))
        return max(abs(val1), abs(val2))
    
    # 480 ms, 76.89%. 1 pass, Time: O(N). Space: O(1)
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sofar = float("-inf")
        min_sofar = float("inf")
        total_sum = total_sub = 0
        for val in nums:
            if total_sum < 0:
                total_sum = 0
            total_sum += val
            max_sofar = max(max_sofar, total_sum)
            
            if total_sub > 0:
                total_sub = 0
            total_sub += val
            min_sofar = min(min_sofar, total_sub)
        return max(abs(min_sofar), abs(max_sofar))
# @lc code=end

