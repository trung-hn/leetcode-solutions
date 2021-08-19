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
   # STEP 1
   # Time: O(2^N). Space: O(N)
    def rob(self, nums: List[int]) -> int:
        def dfs(i):
            if i < 0:
                return 0
            return max(dfs(i - 1), dfs(i - 2) + nums[i])
        return dfs(len(nums) - 1)

    # STEP 2
    # Time and Space: O(N). Top-down approach Dynamic Programming.

    def rob(self, nums: List[int]) -> int:
        mem = {}

        def dfs(i):
            if i in mem:
                return mem[i]
            if i < 0:
                return 0
            mem[i] = max(dfs(i - 1), dfs(i - 2) + nums[i])
            return mem[i]
        return dfs(len(nums) - 1)

    # Time and Space: O(N). Pythonic
    def rob(self, nums: List[int]) -> int:
        @functools.lru_cache
        def dfs(i):
            if i < 0:
                return 0
            return max(dfs(i - 1), dfs(i - 2) + nums[i])
        return dfs(len(nums) - 1)

    # STEP 3. Bottom-up approach Dynamic Programming.
    # Time and Space: O(N)
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        for num in nums:
            dp.append(max(dp[-1], dp[-2] + num))
        return dp[-1]

    # STEP 4
    # 32 ms, 65.46 %. Time O(N). Space: O(1)
    def rob(self, nums: List[int]) -> int:
        prev2 = prev1 = 0
        for num in nums:
            new = max(prev1, prev2 + num)
            prev2, prev1 = prev1, new
        return prev1

# @lc code=end
