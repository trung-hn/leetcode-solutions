#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
# TAGS: Kadane, hard, dynamic programming
# REVIEWME:
class Solution:
    
    # More info in post: https://leetcode.com/problems/maximum-sum-circular-subarray/discuss/178422/One-Pass
    # The key point is `ans = max(the max subarray sum, the total sum - the min subarray sum)`
    # 2 Cases: 1. Maximum in the middle (Similar to normal Kadane)
    #          2. Maximum on both sides => Minumum in the MIDDLE => ans = total - min 


    # 708 ms, 27.99%. Kadane - Sign Variant
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        def kadane(A):
            current = max_subarray = float("-inf")
            for num in A:
                current = num + max(current, 0)
                max_subarray = max(current, max_subarray)
            return max_subarray
        
        S = sum(A)
        max1 = kadane(A)
        max2 = S + kadane(-num for num in A[1:])
        max3 = S + kadane(-num for num in A[:-1])
        return max(max1, max2, max3)
    
    # 676 ms, 33.02%. Kadane - Min Variant
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max1 = current = float("-inf")
        for num in A:
            current = num + max(current, 0)
            max1 = max(current, max1)

        min2 = current = float("inf")
        for num in A[1:]:
            current = num + min(current, 0)
            min2 = min(current, min2)
        max2 = sum(A) - min2
        
        min3 = current = float("inf")
        for num in A[:-1]:
            current = num + min(current, 0)
            min3 = min(current, min3)
        max3 = sum(A) - min3
        
        return max(max1, max2, max3)
    
    # 576 ms, 71%. Lee's solution. Calculate max and min in 1 pass
    def maxSubarraySumCircular(self, A):
        total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
# @lc code=end

