#
# @lc app=leetcode id=1848 lang=python3
#
# [1848] Minimum Distance to the Target Element
#

# @lc code=start
# TAGS: Array


class Solution:
    # 52 ms, 86.17%. Time: O(N). Space: O(1)
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        diff = float("inf")
        for i, num in enumerate(nums):
            if num == target:
                diff = min(diff, abs(i - start))
        return diff
# @lc code=end
