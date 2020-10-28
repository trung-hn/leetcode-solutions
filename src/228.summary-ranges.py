#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
# TAGS: Array
class Solution:
    # 28 ms, 71.93%. Time: O(N). Space: O(1)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        rv = []
        start = nums[0]
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                continue

            end = nums[i]
            if start == end: rv.append(str(start))
            else: rv.append(f"{start}->{end}")
                
            if i < len(nums) - 1: start = nums[i + 1]
        return rv
# @lc code=end

