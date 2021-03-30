#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
# TAGS: Binary Search, Dynamic Programming
# REVIEWME: Binary Search, Dynamic Programming
import bisect


class Solution:
    # Based on article solution. Binary Search + DP
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            i = bisect.bisect_left(lis, num)
            if i >= len(lis):
                lis.append(num)
            else:
                lis[i] = num
        return len(lis)

# @lc code=end
