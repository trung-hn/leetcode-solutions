#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#


# @lc code=start
# TAGS: Dynamic Programming
class Solution:
    # Time: O(N * 900 * 900). 206 ms, 76.08%
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """Thought process. Simulate
        # dp = [][]
        # dp[1] = {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}
        # dp[2] = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:5, 9:4, 10:3, 11:2, 12:1}
        # dp[3] = {1:0, 2:0, 3:1, 4:3, 5:6, 6:10, 7:15, 8: }

        DP using dictionary
        """
        MOD = 10**9 + 7

        # Init DP
        cur = collections.defaultdict(int, {i: 1 for i in range(1, k + 1)})
        for d in range(2, n + 1):
            # New DP
            nxt = collections.defaultdict(int)
            for total in range(d, d * k + 1):
                for part in range(max(1, total - k), total):
                    nxt[total] += cur[part]
                nxt[total] %= MOD
            cur = nxt
        return cur[target]

    # 132 ms, 82.44%.
    # Time, Space: Same as above
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """Optimized version"""
        MOD = 10**9 + 7
        cur = [0] * (target + 1)  # We only care up to target
        for i in range(0, min(k, target) + 1):
            cur[i] = 1

        for d in range(2, n + 1):
            nxt = [0] * (target + 1)
            for total in range(d, min(d * k, target) + 1):
                # d * k because that are all zeroes
                for part in range(max(d - 1, total - k), total):
                    # d - 1 because prior to that are all zeroes
                    # total - k because less than that would make it impossible to sum to total
                    nxt[total] += cur[part]
                nxt[total] %= MOD
            cur = nxt
        return cur[target]  # same as cur[-1]


# @lc code=end
