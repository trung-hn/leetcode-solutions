#
# @lc app=leetcode id=1877 lang=python3
#
# [1877] Minimize Maximum Pair Sum in Array
#
# @lc code=start
# TAGS: Array, Two Pointers, Greedy, Sorting


class Solution:
    # 1224 ms, 56.54%. Time: O(NlogN). Space: O(Sort)
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums) // 2):
            ans = max(ans, nums[i] + nums[~i])
        return ans1
# @lc code=end
