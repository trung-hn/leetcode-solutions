# TAGS: Premium, Math
class Solution:
    # TLE. Time: O(M*M*N*N). Space: O(M*N)
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0: return 0
        
        def bfs(r, c):
            visited = set(); q = collections.deque([[r, c, 0]])
            while q:
                r, c, depth = q.popleft()
                
                if (r, c) in visited: continue
                visited.add((r, c))
                
                distances[r][c] += depth
                
                for x, y in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if 0 <= x < R and 0 <= y < C:
                        q.append((x, y, depth + 1))
        
        R = len(grid); C = len(grid[0])
        houses = [(r, c) for r in range(R) for c in range(C) if grid[r][c]]
        distances = [[0] * C for _ in range(R)]
        for r, c in houses:
            bfs(r, c)
        
        return min(val for row in distances for val in row)
    
    # Using Median: 
    # As long as there is equal number of points to the left and right of the meeting point, the total distance is minimized.
    # 60 ms, 86.78%. Time: O(M*N). Space: O(M + N)
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0: return 0
        
        R = len(grid); C = len(grid[0])
        rows = [r for r in range(R) for c in range(C) if grid[r][c]]
        cols = [c for c in range(C) for r in range(R) if grid[r][c]]
        
        median_row = rows[len(rows) // 2]
        median_col = cols[len(cols) // 2]
        
        ans = 0
        for r, c in zip(rows, cols):
            ans += abs(r - median_row) + abs(c - median_col)
        return ans
    