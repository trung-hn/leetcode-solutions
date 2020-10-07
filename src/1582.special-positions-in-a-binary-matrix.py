#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#

# @lc code=start
# TAGS: Array
class Solution:
    # 164 ms, 96.86%. Time and Space: O(N)
    def numSpecial(self, mat: List[List[int]]) -> int:
        sum_of_rows = [sum(row) for row in mat]
        sum_of_cols = [sum(col) for col in zip(*mat)]
        ans = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == sum_of_cols[c] == sum_of_rows[r] == 1: 
                    ans += 1
        return ans
# @lc code=end

