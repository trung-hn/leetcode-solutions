#
# @lc app=leetcode id=1992 lang=python3
#
# [1992] Find All Groups of Farmland
#

# @lc code=start
# TAGS: Array, DFS, BFS, Matrix
from typing import List


class Solution:
    # 1208 ms, 90.88%. Time and Space: O(R*C)
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        def find_lower_right(r, c):
            while r < R - 1 and land[r + 1][c]:
                r += 1
            while c < C - 1 and land[r][c + 1]:
                c += 1
            return r, c

        def sink(ur, uc, lr, lc):
            for r in range(ur, lr + 1):
                for c in range(uc, lc + 1):
                    land[r][c] = 0

        ans = []
        R, C = len(land), len(land[0])
        for r in range(R):
            for c in range(C):
                if land[r][c] == 0:
                    continue
                lr, lc = find_lower_right(r, c)
                ans.append([r, c, lr, lc])
                sink(r, c, lr, lc)
        return ans

# @lc code=end
