# TAGS: BFS, Premium
class Solution:
    # 848 ms, 40.41%. Time and Space: O(N*M)
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        def bfs(r, c):
            visited = set(); q = collections.deque([(r, c, 0)])
            while q:
                r, c, depth = q.popleft()
                if (r, c) in visited: continue
                visited.add((r, c))
                
                if grid[r][c] <= 0:
                    grid[r][c] -= depth
                    freq[r][c] += 1

                for x, y in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if  0 <= x < R and 0 <= y < C and grid[x][y] <= 0:
                        q.append((x, y, depth + 1))
        
        R = len(grid); C = len(grid[0])
        houses = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == 1]
        freq = [[0]*C for _ in range(R)]
        for r, c in houses: 
            bfs(r, c)
               
        best_house = -1
        for r in range(R):
            for c in range(C):
                if grid[r][c] in (0, 1, 2): continue
                if freq[r][c] != len(houses): continue
                if -grid[r][c] < best_house or best_house == -1:
                    best_house = -grid[r][c]
            
        return best_house
        