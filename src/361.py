# TAGS: Premium, Dynamic Programming
class Solution:
    # 356 ms 64.43%. Time and Space: O(N*M)
    # Calculate pre and post fix sum and then find max
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        R, C = len(grid), len(grid[0])
        prefix_row = [[0] for _ in range(R)]
        postfix_row = [[0] for _ in range(R)]
        prefix_col = [[0] for _ in range(C)]
        postfix_col = [[0] for _ in range(C)]
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "W":
                    prefix_row[r].append(0)
                    prefix_col[c].append(0)
                elif grid[r][c] == "E":
                    prefix_row[r].append(prefix_row[r][-1] + 1)
                    prefix_col[c].append(prefix_col[c][-1] + 1)
                else:
                    prefix_row[r].append(prefix_row[r][-1])
                    prefix_col[c].append(prefix_col[c][-1])
                    
                if grid[r][~c] == "W":
                    postfix_row[r].append(0)
                elif grid[r][~c] == "E":
                    postfix_row[r].append(postfix_row[r][-1] + 1)
                else:
                    postfix_row[r].append(postfix_row[r][-1])
                    
                if grid[~r][c] == "W":
                    postfix_col[c].append(0)
                elif grid[~r][c] == "E":
                    postfix_col[c].append(postfix_col[c][-1] + 1)
                else:
                    postfix_col[c].append(postfix_col[c][-1])
        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "0":
                    ans = max(ans, prefix_row[r][c] + postfix_row[r][~c] + prefix_col[c][r] + postfix_col[c][~r])
        return ans
    
    # 312 ms, 86.55%. Time and Space: O(N*M). Similar to above
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        R, C = len(grid), len(grid[0])
        matrix = [[0]*C for _ in range(R)]
        
        for r in range(R):
            prefix = postfix = 0
            for c in range(C):
                if grid[r][c] == "W": prefix = 0
                elif grid[r][c] == "E": prefix += 1
                else: matrix[r][c] += prefix
                
                if grid[r][~c] == "W": postfix = 0
                elif grid[r][~c] == "E": postfix += 1
                else: matrix[r][~c] += postfix
        
        for c in range(C):
            prefix = postfix = 0
            for r in range(R):
                if grid[r][c] == "W": prefix = 0
                elif grid[r][c] == "E": prefix += 1
                else: matrix[r][c] += prefix
                
                if grid[~r][c] == "W": postfix = 0
                elif grid[~r][c] == "E": postfix += 1
                else: matrix[~r][c] += postfix
        return max(val for row in matrix for val in row)