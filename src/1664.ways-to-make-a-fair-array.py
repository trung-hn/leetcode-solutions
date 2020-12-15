#
# @lc app=leetcode id=1664 lang=python3
#
# [1664] Ways to Make a Fair Array
#

# @lc code=start
# TAGS: Dynamic Programming, Greedy
class Solution:
    # 1472 ms, 47.06%. Time: O(N). Space: O(N)
    def waysToMakeFair(self, nums: List[int]) -> int:
        mem = [[0,0]]
        for i, val in enumerate(nums):
            if i % 2: mem.append([mem[-1][0], mem[-1][1] + val])
            else:     mem.append([mem[-1][0] + val, mem[-1][1]])
        
        ans = 0
        for (prev_even, prev_odd), (cur_even, cur_odd) in zip(mem, mem[1:]):
            total_odd = prev_odd + mem[-1][0] - cur_even
            total_even = prev_even + mem[-1][1] - cur_odd
            if total_odd == total_even:
                ans += 1
        return ans
    
    # 1244 ms, 81.48%. Time: O(N). Space: O(1)
    def waysToMakeFair(self, nums: List[int]) -> int:
        odds = sum(nums[1::2])
        evens = sum(nums[::2])
        cur = [0, 0]; ans = 0 
        for i, val in enumerate(nums):
            prev_even, prev_odd = cur
            cur[i % 2] += val
            total_odd = prev_odd + evens - cur[0]
            total_even = prev_even + odds - cur[1]
            if total_odd == total_even:
                ans += 1
        return ans
# @lc code=end

