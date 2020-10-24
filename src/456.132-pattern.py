#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
# TAGS: Stack
# REVIEWME: Stack, Hard
class Solution:
    # 99.18%. Time and Space: O(N)
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mid = float('-inf')
        for num in reversed(nums):
            if num < mid: return True
            while stack and stack[-1] < num:
                mid = stack.pop()
            stack.append(num)
        return False
# @lc code=end

