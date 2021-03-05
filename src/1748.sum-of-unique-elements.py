#
# @lc app=leetcode id=1748 lang=python3
#
# [1748] Sum of Unique Elements
#

# @lc code=start
# TAGS: Array, Hash Table


class Solution:
    # 36 ms, 68.56%. Time and Space: O(N)
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        total = 0
        for v, f in counter.items():
            if f == 1:
                total += v
        return total
# @lc code=end
