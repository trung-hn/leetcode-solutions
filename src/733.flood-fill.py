#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
# TAGS: dfs, 
class Solution:
    # 76 ms, 80%. O(N), O(N)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(r, c, new_color):
            old_color, image[r][c] = image[r][c], new_color
            for i, j in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0<= i < R and 0<= j < C and image[i][j] == old_color:
                    dfs(i,j, new_color)
        R, C = len(image), len(image[0])
        if newColor != image[sr][sc]: dfs(sr, sc, newColor)
        return image
# @lc code=end

