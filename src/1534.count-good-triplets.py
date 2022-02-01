#
# @lc app=leetcode id=1534 lang=python3
#
# [1534] Count Good Triplets
#

# @lc code=start
# TAGS: Array, Enumeration
from typing import List


class Solution:
    # Time: O(N^3). Space: O(N)
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    ans += (abs(arr[i] - arr[j]) <= a) \
                        and (abs(arr[j] - arr[k]) <= b) \
                        and (abs(arr[k] - arr[i]) <= c)
        return ans
# @lc code=end
