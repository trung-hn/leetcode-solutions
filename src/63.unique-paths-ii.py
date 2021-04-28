#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
# TAGS: Array, Dynamic Programming


class Solution:
    # Time: O(M*N). Space: O(M). Bottom up DP
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * (C + 1)
        dp[1] = 1
        for r in range(R):
            nxt = [0]
            for c in range(C):
                if obstacleGrid[r][c]:
                    nxt.append(0)
                else:
                    nxt.append(nxt[-1] + dp[c + 1])
            dp = nxt
        return dp[-1]

# @lc code=end
