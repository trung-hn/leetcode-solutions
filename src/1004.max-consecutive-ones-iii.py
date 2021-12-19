#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
# TAGS: Sliding Window, Two Pointers
from typing import List


class Solution:
    # 652 ms, 41.04%
    # Easy to understand solition
    def longestOnes(self, A: List[int], k: int) -> int:
        ptr = ans = 0
        for i, n in enumerate(A):
            if not n:
                while not k:
                    k += A[ptr] == 0
                    ptr += 1
                k -= 1
            ans = max(ans, i + 1 - ptr)
        return ans

    # 564 ms, 86.48%
    # Over simplified of the version above. Very clever but hard to understand
    # We never decrease the size of the window
    # K is used as the offset.
    # if K is positive, we can always increase the window size
    # if K is negative, we increase K (if applicable) and this it as offset at the end
    # at some point, K might turn back to positive again, at which time the offset reduce to 0
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        for right in range(len(A)):
            K -= A[right] == 0

            if K < 0:
                K += A[left] == 0
                left += 1

        return right - left + 1

# @lc code=end
