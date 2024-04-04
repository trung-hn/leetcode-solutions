#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#


# @lc code=start
# TAGS: Math, Backtracking, Bit Manipulation
class Solution:
    # Time and Space: O(2^N)
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(n):
            highest_bit = 1 << i
            for j in reversed(range(highest_bit)):
                ans.append(ans[j] + highest_bit)
        return ans


# @lc code=end
