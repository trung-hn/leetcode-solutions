#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#

# @lc code=start
# TAGS: Array
class Solution:

    # 152 ms, 10.37%. Time and Space: O(N)
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [v for v in A if v % 2 == 0] + [v for v in A if v % 2]

    # 136 ms, 16.81%. Time: O(N), Space: O(1)
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        while left < right:
            while A[left] % 2 == 0 and left < right:
                left += 1
            while A[right] % 2 and left < right:
                right -= 1
            A[left], A[right] = A[right], A[left]
        return A

# @lc code=end

