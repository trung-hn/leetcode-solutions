#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#

# @lc code=start
# TAGS: Binary Search, DFS, BFS, Union Find, Graph
class Solution:
    # dfs
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def dfs(r=0, c=0, limit=0):
            visited.add((r, c))
            for i, j in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                if 0 <= i < R and 0 <= j < C and (i, j) not in visited:
                    if abs(heights[i][j] - heights[r][c]) <= limit:
                        dfs(i, j, limit)
        
        R, C = len(heights), len(heights[0])
        left = 0; right = 10**6
        while left < right:
            mid = (left + right) // 2
            visited = set()
            dfs(limit=mid)
            if (R - 1, C - 1) in visited: right = mid
            else: left = mid + 1
        return left
    
    # bfs
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def bfs(limit):
            visited = set()
            q = [(0, 0)]
            while q:
                cur = set()
                for r, c in q:
                    visited.add((r, c))
                    for i, j in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                        if 0 <= i < R and 0 <= j < C and (i, j) not in visited:
                            if abs(heights[i][j] - heights[r][c]) <= limit:
                                cur.add((i, j))
                q = cur
            return visited
        
        R, C = len(heights), len(heights[0])
        left = 0; right = 10**6
        while left < right:
            mid = (left + right) // 2
            if (R - 1, C - 1) in bfs(limit=mid): right = mid
            else: left = mid + 1
        return left
# @lc code=end

