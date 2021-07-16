#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
# TAGS: Array, Two Pointers, Binary Search, Greedy, Sorting
# REVIEWME: Two Pointers, Greedy


class Solution:
    # 1140 ms, 64.29%. Time: O(N^2). Space: O(1)
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for k in range(2, len(nums)):
            i, j = 0, k - 1
            while j > i:
                if nums[i] + nums[j] > nums[k]:
                    total += j - i
                    j -= 1
                else:
                    i += 1
        return total
# @lc code=end
