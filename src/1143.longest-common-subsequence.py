#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
# TAGS: String, Dynamic Programming


class Solution:
    # 908 ms, 17.75%. Gene alignment. Time and Space: O(M*N).
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        R = len(text1)
        C = len(text2)
        grid = [[0] * (C + 1) for _ in range(R + 1)]

        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if text1[r - 1] == text2[c - 1]:
                    grid[r - 1][c - 1] += 1
                grid[r][c] = max(grid[r - 1][c - 1], grid[r - 1][c], grid[r][c - 1])
        return grid[-1][-1]

    # Further optimize because we only need 2 rows at a time.
    # 528 ms, 34.82%. Time: O(M*N) Space: O(M + N)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1
        R = len(text1) + 1
        C = len(text2) + 1
        prev = [0] * C
        cur = [0] * C

        skip_cost = subs_cost = 0  # Usually negative
        match = 1

        for r in range(1, R):
            for c in range(1, C):
                if text1[r - 1] == text2[c - 1]:
                    prev[c - 1] += match
                else:
                    prev[c - 1] += subs_cost
                cur[c] = max(prev[c - 1] + skip_cost, prev[c], cur[c - 1] + skip_cost)
            prev = cur
            cur = [0] * C
        return prev[-1]


# @lc code=end
