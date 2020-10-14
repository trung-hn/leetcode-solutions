#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
# TAGS: Dynamic Programming
class Solution:
    """
    Similar to House Robber I but the key thing here is the first house is next to the last house. 
    These fore, we split it into 2 cases: rob from 0 to n - 1 and 1 to n
    """
    # 32 ms, 68.99%. Time: O(N). Space: O(1)
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        def rob_me(nums):
            rob = not_rob = 0
            for house in nums:
                temp = rob
                rob = not_rob + house
                not_rob = max(temp, not_rob)
            return max(rob, not_rob)
        return max(rob_me(nums[:-1]), rob_me(nums[1:]))

# @lc code=end

