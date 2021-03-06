#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
# TAGS: Array, Greedy
# REVIEWME: Greedy


class Solution:
    """
    Approach:
    Greedy: we have left and right pointers which are the limit at each step
    left and right will change based on max(nums[left:right])
    Keep doing it until right == len(nums) - 1
    """
    # 32 ms. 68.42%. Time: O(N^2). Space: O(N). Backward DP

    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[-1] = 0
        for i in reversed(range(len(nums) - 1)):
            num = nums[i]
            if num:
                dp[i] = min(dp[i + 1: i + num + 1]) + 1
        return dp[0]

    # 32 ms. 68.42%. Time: O(N^2). Space: O(N). forward DP
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for i, num in enumerate(nums):
            for j in range(i + 1, min(i + num + 1, len(nums))):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]

    # Greedy. 28 ms, 88.39%. Time: O(N). Space: O(1)
    def jump(self, nums: List[int]) -> int:
        step = left = right = 0
        while right < len(nums) - 1:
            step += 1
            nxt = max(j + nums[j] for j in range(left, right + 1))
            left, right = right, nxt
        return step
# @lc code=end
