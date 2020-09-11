#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
# TAGS: Dynamic Programming, Array
# REVIEWME: Dynamic Programming
class Solution:
    # TLE Bruteforce. Time: O(N^2), Space: O(1)
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            product = 1
            for val in nums[i:]:
                product *= val
                ans = max(ans, product)
        return ans

    # 52 ms, 91.37%. First Solution. Time: O(N). Space: O(N)
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        max_val = float("-inf")
        zeroes = [-1] + [i for i, v in enumerate(nums) if v == 0] + [len(nums)]
        
        # Ranges bounded by zeroes
        for z1, z2 in zip(zeroes, zeroes[1:]):

            # Calculate cummulative product until the first neg number
            first_neg = 1
            arg = z2 - 1
            for index in range(z1 + 1, z2):
                first_neg *= nums[index]
                max_val = max(max_val, first_neg)
                if first_neg < 0:
                    arg = index
                    break
            cur = 1
            multiplied = False
            for i in range(arg + 1, z2):
                cur *= nums[i]
                if cur < 0: 
                    if not multiplied: cur *= first_neg
                    else: cur /= first_neg
                    multiplied = not multiplied
                max_val = max(max_val, int(cur))
        return max(max_val, 0)
        
    # 52 ms, 81%. Solution by lee
    # https://leetcode.com/problems/maximum-product-subarray/discuss/183483/JavaC%2B%2BPython-it-can-be-more-simple
    def maxProduct(self, A: List[int]) -> int:
        B = list(reversed(A))
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1 # prefix
            B[i] *= B[i-1] or 1 # suffix
            # A[i-1] equals 0 when the sequence resets. If that's the case, we multiply with 1 instead. 
        print(A, B)
        return max(A + B) if A else 0 # Notice this is sum of array 
    
    # 44 ms, 98%. Still not sure 100%
    def maxProduct1(self, nums: List[int]) -> int:
        if not nums: return 0
        max_sofar = min_sofar = max_global = nums[0]
        for num in nums[1:]:
            if num < 0: # Switch max, min when they change side. 
                max_sofar, min_sofar = min_sofar, max_sofar
            max_sofar = max(max_sofar * num, num)
            min_sofar = min(min_sofar * num, num)
            max_global = max(max_global, max_sofar)
        return max_global

# @lc code=end

