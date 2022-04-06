#
# @lc app=leetcode id=1980 lang=python3
#
# [1980] Find Unique Binary String
#

# @lc code=start
# TAGS: binary-search, string
from typing import List


class Solution:
    # 28 ms, 98.70%. Time: O(NlogN), Space: O(N)
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def to_num(s):
            ans = 0
            for c in s:
                ans = ans * 2 + bool(c == "1")
            return ans

        def binary_search():
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if to_num(nums[mid]) > mid:
                    hi = mid
                else:
                    lo = mid + 1

            # [0, 1, 3, 4]
            if to_num(nums[lo]) > lo:
                num = to_num(nums[lo]) - 1
                return f'{num:0{N}b}'

            # [0, 1, 2, 3]
            num = to_num(nums[lo]) + 1
            return f'{num:0{N}b}'

        N = len(nums[0])
        nums.sort()
        return binary_search()
# @lc code=end
