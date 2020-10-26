#
# @lc app=leetcode id=799 lang=python3
#
# [799] Champagne Tower
#

# @lc code=start
# TAGS: Dynamic Programming
# REVIEWME: Dynamic Programming

import functools
class Solution:
    # 84 ms, 92%. Time: O(R^2). Space:(R^2)
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        self.poured = poured

        @functools.lru_cache(None)
        def dfs(query_row, query_glass):

            if query_row == query_glass == 0:
                return self.poured
            
            if query_glass == 0 or query_glass == query_row:
                above = dfs(query_row - 1, 0)
                return (above - 1) / 2 if above > 1 else 0
            
            left = dfs(query_row - 1, query_glass - 1)
            left = (left - 1) / 2 if left > 1 else 0
            
            right = dfs(query_row - 1, query_glass)
            right = (right - 1) / 2 if right > 1 else 0
            
            return left + right

        return min(1, dfs(query_row, query_glass))
    # 96 ms, 84%. Time: O(R^2). Space:(R^2)
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * i for i in range(1, 102)]
        tower[0][0] = poured

        for r in range(query_row + 1):
            for c in range(r + 1):
                extra = (tower[r][c] - 1) / 2
                if extra > 0:
                    tower[r + 1][c] += extra
                    tower[r + 1][c + 1] += extra
        return min(1, tower[query_row][query_glass])

# @lc code=end

