#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
# TAGS: BFS
class Solution:
    # 888 ms, 23.81%. Time and Space: O(N)
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        N = len(grid)
        visited = set()
        depth = 0
        q = [(0, 0)]
        while q:
            cur = set()
            depth += 1
            for r, c in q:
                if r == c == N - 1:
                    return depth
                visited.add((r, c))
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == dc == 0: continue
                        x = r + dr; y = c + dc
                        if (x, y) in visited: continue
                        if x < 0 or y < 0 or x >= N or y >= N: continue
                        if grid[x][y] == 0:
                            cur.add((x, y))
            q = cur
        return -1
                
# @lc code=end

