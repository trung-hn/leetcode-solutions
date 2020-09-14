#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
# TAGS: Dynamic Programming
# REVIEWME: Dynamic Programming, lru_cache
import functools
class Solution:
    # 16 ms, 99%. First solution
    def rob(self, nums: List[int]) -> int:
        # first is only pick first house, 
        # second is only pick second house. 
        # third is not picking any house
        profit = nums[:2] + [0]
        for i in range(2, len(nums), 2):
            temp = []
            temp.append(max(profit[0], profit[-1]) + nums[i])
            if i < len(nums) - 1:
                temp.append(max(profit[:2]) + nums[i+1])
            temp.append(max(profit))
            profit = temp
        return max(profit)
    
    # 32 ms, 65.46 %. Cleanest soltion. Time O(N). Space: O(1)
    def rob(self, nums: List[int]) -> int:
        # At any house, we can either rob or don't rob
        # rob this house = not robbing the previous house + curr
        # not robbing this house = max(robbing previous house, not robbing previous house. )
        
        rob = not_rob = 0
        for num in nums:
            temp_rob = rob
            rob = not_rob + num
            not_rob = max(temp_rob, not_rob)
        return max(rob, not_rob)

    # 32 ms, 65.46 %. Memoization using lru_cache. Time and Space: O(N) because of the memory. 
    def rob(self, nums: List[int]) -> int:
        @functools.lru_cache
        def dfs(i):
            if i < 0: return 0
            return max(dfs(i - 1), dfs(i - 2) + nums[i])
        return dfs(len(nums) - 1)
# @lc code=end

