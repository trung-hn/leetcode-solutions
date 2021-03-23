#
# @lc app=leetcode id=1444 lang=python3
#
# [1444] Number of Ways of Cutting a Pizza
#

# @lc code=start
# TAGS: Dynamic Programming


class Solution:
    """
    edge case:
    [1 1 1]
    [0 0 0]
    [1 1 1]
    [0 0 0]
    """
    # 264 ms, 64.44%. Time: O(K*R*C*(R+C)). Space: O(K*M*N)

    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        R, C = len(pizza), len(pizza[0])
        # Get post fix sum calculate from bottom right
        post_sum = [[0] * (C + 1) for _ in range(R + 1)]
        for r in reversed(range(R)):
            for c in reversed(range(C)):
                post_sum[r][c] = post_sum[r + 1][c] + post_sum[r][c +
                                                                  1] - post_sum[r + 1][c + 1] + bool(pizza[r][c] == 'A')

        @cache
        def dfs(r0, c0, cut):
            if post_sum[r0][c0] == 0:
                return 0
            if cut == 0:
                return 1
            rv = 0
            # Cut by row (horizontally)
            for r in range(r0, R):
                # We cannot just consider that row, because of edge case: empty row, non empty row, empty row
                # We can cut at the second empty row as well
                if post_sum[r0][c0] - post_sum[r + 1][c0] <= 0:
                    continue
                rv += dfs(r + 1, c0, cut - 1) % MOD

            # cut by column (vertically)
            for c in range(c0, C):
                if post_sum[r0][c0] - post_sum[r0][c + 1] <= 0:
                    continue
                rv += dfs(r0, c + 1, cut - 1) % MOD

            return rv % MOD
        return dfs(0, 0, k - 1) % MOD

# @lc code=end
