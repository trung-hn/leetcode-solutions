#
# @lc app=leetcode id=1035 lang=python3
#
# [1035] Uncrossed Lines
#

# @lc code=start
# TAGS: Array, Dynamic Programming
# REVIEWME: Needleman–Wunsch algorithm
class Solution:
    """
    Things to be careful about: 
    Copy list like this `prev = cur[:]` not `prev = cur`
    Index of i and j (+-1)z
    """
    # 256 ms, 53.05% . Time and Space: O(N^2)
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        grid = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    grid[i][j] += 1
                grid[i + 1][j + 1] = max(grid[i][j], grid[i][j+1], grid[i+1][j])
        return grid[-1][-1]

    # 204 ms, 91.78% . Time: O(N^2). Space: O(N)
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        prev = [0] * (len(B) + 1)
        cur = [0] * (len(B) + 1)
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    prev[j] += 1
                cur[j + 1] = max(prev[j], prev[j+1], cur[j])
            prev = cur[:]
        return cur[-1]

# @lc code=end

