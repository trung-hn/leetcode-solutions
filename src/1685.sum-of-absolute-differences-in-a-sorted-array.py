#
# @lc app=leetcode id=1685 lang=python3
#
# [1685] Sum of Absolute Differences in a Sorted Array
#

# @lc code=start
# TAGS: Math, Greedy
class Solution:
    # 960 ms, 68.22 %. Time and Space: O(N)
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        ans = []
        prefix_sum = 0
        for i, num in enumerate(nums, 1):
            prefix_sum += num
            postfix_sum = total - prefix_sum
            val = postfix_sum - (len(nums) - i) * num + i * num - prefix_sum
            ans.append(val)
        return ans
# @lc code=end

