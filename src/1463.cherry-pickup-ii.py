#
# @lc app=leetcode id=1463 lang=python3
#
# [1463] Cherry Pickup II
#

# @lc code=start
# TAGS: Dynamic Programming
class Solution:
    """
    How to think about this problem. Instead of thinking about how the robots go down, we can think about how the robots go up
    For example, if we have only 1 row, we have the answer right away
    if we have 2 rows, there are 4 cases to think about (because robots start at corners)

    If we keep increasing rows, you can see that we can dp through all cases.

    The first solution below is WIP and i failed to finish because it was very complicated to think about how robots go down
    The other 2 solutions follow the logic explained above.
    """
    # WIP
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dp = [[[0 for _ in range(C)] for _ in range(C)] for _ in range(R)]
        dp[0][0][-1] = grid[0][0] + grid[0][-1]
        for r in range(R - 1):
            for c1 in range(C):
                for c2 in range(C):
                    for dc1 in (-1, 0, 1):
                        for dc2 in (-1, 0, 1):
                            new_c1 = c1 + dc1
                            new_c2 = c2 + dc2
                            # if new_c2 < new_c1: continue
                            if new_c1 < 0 or new_c1 >= C or new_c2 < 0 or new_c2 >= C: continue
                            
                            robot1 = grid[r + 1][new_c1]
                            robot2 = grid[r + 1][new_c2]
                            
                            if new_c1 == new_c2: 
                                collect_this_row = dp[r][c1][c2] + max(robot1, robot2)
                            else:
                                collect_this_row = dp[r][c1][c2] + robot1 + robot2
                            dp[r + 1][c1 + dc1][c2 + dc2] = max(dp[r + 1][c1 + dc1][c2 + dc2], collect_this_row)
                            # print(dp[r][c1][c2], dp[r + 1][c1 + dc1][c2 + dc2])
        from pprint import pprint
        # pprint(dp)
        return max(dp[-1][c1][c2] for c1 in range(C) for c2 in range(C))
    
    # 88.87%. DP topdown with memo. Time and Space: O(R*C*C)
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        @lru_cache(None)
        def dp(row, col1, col2):
            if col1 < 0 or col1 >= C or col2 < 0 or col2 >= C:
                return 0
            if row >= R: return 0
            
            collect = grid[row][col1]
            if col1 != col2:
                collect += grid[row][col2]
            
            return collect + max(dp(row + 1, new_col1, new_col2) 
                                 for new_col1 in (col1 - 1, col1, col1 + 1)
                                 for new_col2 in (col2 - 1, col2, col2 + 1))
        return dp(0, 0, C - 1)
    
    # DP bottom up
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[0]*n for _ in range(n)] for __ in range(m)]

        for row in reversed(range(m)):
            for col1 in range(n):
                for col2 in range(n):
                    result = 0
                    # current cell
                    result += grid[row][col1]
                    if col1 != col2:
                        result += grid[row][col2]
                    # transition
                    if row != m-1:
                        result += max(dp[row+1][new_col1][new_col2]
                                      for new_col1 in [col1, col1+1, col1-1]
                                      for new_col2 in [col2, col2+1, col2-1]
                                      if 0 <= new_col1 < n and 0 <= new_col2 < n)
                    dp[row][col1][col2] = result
        return dp[0][0][n-1]
# @lc code=end

