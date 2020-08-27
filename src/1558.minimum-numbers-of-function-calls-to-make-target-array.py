#
# @lc app=leetcode id=1558 lang=python3
#
# [1558] Minimum Numbers of Function Calls to Make Target Array
#

# @lc code=start
# TAGS: Greedy, Simulation
class Solution:
    """
    The tactics is simple, because we cannot perform *2 when we have odd number in the array,
    we have to -1 to all odd numbers first. 
    """
    # 1196 ms, 67.43 %. Time: O(NlogK). Space: O(N), N is the length of nums and K is the max in nums
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        while 1:
            # -1 to all odd numbers
            op += sum(num % 2 for num in nums)
            nums = [num - 1 if num % 2 else num for num in nums ]
            
            if not any(nums): break
            # /2 to all even numbers. 
            nums = [num // 2 for num in nums]
            op += 1
        return op

    # Bit count solution from lee215: 
    # https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/discuss/805740/JavaC%2B%2BPython-Bit-Counts
    # Space: O(1)
    def minOperations(self, nums: List[int]) -> int:
        return sum(bin(a).count('1') for a in A) + len(bin(max(A))) - 3
        
# @lc code=end

