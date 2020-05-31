#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
# TAGS: String, Dynamic Programming
# REVIEWME: think gene alignment
class Solution:
    # 200 ms, 50%. Time and Space: O(M * N)
    def minDistance(self, word1: str, word2: str) -> int:
        X, Y = len(word1) + 1, len(word2) + 1
        grid = [[0] * X for _ in range(Y)]
        
        for i in range(1, X):
            grid[0][i] = grid[0][i - 1] + 1
        for i in range(1, Y):
            grid[i][0] = grid[i - 1][0] + 1
        
        for x in range(1, X):
            for y in range(1, Y):
                if word1[x-1] == word2[y-1]: 
                    grid[y][x] = min(grid[y-1][x] + 1, grid[y][x-1] + 1, grid[y-1][x-1])
                else:
                    grid[y][x] = min(grid[y-1][x] + 1, grid[y][x-1] + 1, grid[y-1][x-1] + 1)
        return grid[-1][-1]

    # 164 ms, 80.92%. Time: O(M * N). Space: O(N)
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2: return len(word1 or word2) 
        X, Y = len(word1) + 1, len(word2) + 1

        prev = list(range(X))
        cur = [0] * X
        for y in range(1, Y):
            cur[0] = y
            for x in range(1, X):
                if word1[x-1] == word2[y-1]: 
                    cur[x] = min(prev[x] + 1, cur[x-1] + 1, prev[x-1])
                else:
                    cur[x] = min(prev[x] + 1, cur[x-1] + 1, prev[x-1] + 1)
            prev = cur[:]
        return cur[-1]
                
# @lc code=end

