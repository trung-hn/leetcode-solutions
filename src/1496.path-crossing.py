#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
#

# @lc code=start
class Solution:
    # 24 ms, 95.26%. Time and Space: O(N)
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        x = y = 0
        for di in path:
            visited.add((x, y))
            if di == "N": y += 1
            elif di == "S": y -= 1
            elif di == "E": x += 1
            elif di == "W": x -= 1
            if (x, y) in visited:
                return True
        return False

# @lc code=end

