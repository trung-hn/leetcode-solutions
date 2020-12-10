#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
# TAGS: Array
class Solution:
    # 196 ms, 50.26%. Time and Space: O(R*C)
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        ans = []
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(C):
                pos = r + c
                if pos >= len(ans):
                    ans.append([])
                ans[pos].append(matrix[r][c])
        return [val for i, row in enumerate(ans) 
                for val in (row if i % 2 else reversed(row))]
        
# @lc code=end

