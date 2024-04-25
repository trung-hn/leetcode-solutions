#
# @lc app=leetcode id=2824 lang=python3
#
# [2824] Count Pairs Whose Sum is Less than Target
#


# @lc code=start
# TAGS: Array, Two Pointers, Binary Search, Sorting
class Solution:
    # Time: O(NlogN). Space: O(1)
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left = ans = 0
        for right in reversed(range(len(nums))):
            while left < right and nums[left] + nums[right] < target:
                left += 1
            ans += min(left, right)
        return ans


# @lc code=end
