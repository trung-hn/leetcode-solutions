#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
# TAGS: Array, Two Pointers
class Solution:
	# 68 ms, 99.66%. Time and Space: O(N)
    def findPairs(self, nums: List[int], k: int) -> int:
        C = collections.Counter(nums)
        if k == 0:
            return sum(val > 1 for val in C.values())
        return sum(num + k in C for num in C)
# @lc code=end

