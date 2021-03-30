#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#

# @lc code=start
# TAGS: String, Dynamic Programming
import collections


class Solution:
    # 100 ms, 5.79%. Time: O(N*M). Space: O(M)
    def numDistinct(self, s: str, t: str) -> int:
        # First Step, matching string (similar to gene)
        N, M = len(t), len(s)
        source = collections.defaultdict(list)
        dp = [0] * (M + 1)
        for n, c1 in enumerate(t, 1):
            cur = [float("-inf")]
            for m, c2 in enumerate(s, 1):
                upper_left = dp[m - 1]
                prev = cur[-1]
                # Different characters or same but 2 ways
                if c1 != c2 or upper_left + 1 < prev:
                    source[(n, m)] = [(n, m - 1)]
                    cur.append(prev)
                # Source from upper_left
                elif upper_left + 1 > prev:
                    source[(n, m)] = [(n - 1, m - 1)]
                    cur.append(upper_left + 1)
                # Source from prev
                else:
                    source[(n, m)] = [(n, m-1), (n - 1, m-1)]
                    cur.append(prev)
            dp = cur

        # Second step, trace back and count
        @cache
        def dfs_count(cell):
            # cell is first row of dp
            if cell[0] == 0:
                return 1
            return sum(dfs_count(s) for s in source[cell])
        return dfs_count((N, M))

    # 40 ms, 83.08%. Time: O(N*M). Space: O(M)
    def numDistinct(self, s: str, t: str) -> int:
        N, M = len(t), len(s)
        source = collections.defaultdict(list)
        dp = [1] * (M + 1)
        for n, c1 in enumerate(t, 1):
            cur = [0]
            for m, c2 in enumerate(s, 1):
                upper_left = dp[m - 1]
                prev = cur[-1]
                if c1 != c2:
                    cur.append(prev)
                else:
                    cur.append(prev + upper_left)
            dp = cur
        return dp[-1]

# @lc code=end
