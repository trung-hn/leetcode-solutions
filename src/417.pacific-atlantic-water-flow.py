#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
# TAGS: DFS, BFS
# REVIEWME: DFS, BFS


class Solution:
    """
    Note: Have to start from ocean. If we do it from land, there can be many problem 
    """
    # 276 ms, 84.64%. Time and Space: O(R*C) BFS

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pacific_reachable = set()
        atlantic_reachable = set()

        if not matrix:
            return []

        def bfs(r, c, visited):
            q = [(r, c)]
            for r, c in q:
                if (r, c) in visited:
                    continue
                visited.add((r, c))
                for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if (nr, nc) in visited:
                        continue
                    if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] >= matrix[r][c]:
                        q.append((nr, nc))

        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            bfs(r, 0, pacific_reachable)
            bfs(r, C - 1, atlantic_reachable)

        for c in range(C):
            bfs(0, c, pacific_reachable)
            bfs(R - 1, c, atlantic_reachable)

        return pacific_reachable & atlantic_reachable

    # 264 ms, 96.88%. Time and Space: O(R*C) DFS
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        pacific_reachable = set()
        atlantic_reachable = set()

        if not matrix:
            return []

        def dfs(r, c, visited):
            visited.add((r, c))
            for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if (nr, nc) in visited:
                    continue
                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] >= matrix[r][c]:
                    dfs(nr, nc, visited)

        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            dfs(r, 0, pacific_reachable)
            dfs(r, C - 1, atlantic_reachable)

        for c in range(C):
            dfs(0, c, pacific_reachable)
            dfs(R - 1, c, atlantic_reachable)

        return pacific_reachable & atlantic_reachable


# @lc code=end
