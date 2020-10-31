#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#

# @lc code=start
# TAGS: Math
class Solution:
    # 72 ms, 78.59%. Time: O(NlogN). Space: O(N). Median
    def minMoves2(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        median = nums[len(nums)//2]
        return sum(abs(val - median) for val in nums)
# @lc code=end

