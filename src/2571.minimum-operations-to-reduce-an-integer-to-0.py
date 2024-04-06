#
# @lc app=leetcode id=2571 lang=python3
#
# [2571] Minimum Operations to Reduce an Integer to 0
#


# @lc code=start
# TAGS: Dynamic Programming, Greedy, Bit Manipulation


class Solution:
    def minOperations(self, n: int) -> int:
        def next_n(n):
            mn = float("inf")
            for power in powers:
                diff = n + (power if n < 0 else -power)
                if abs(diff) > abs(mn):
                    return mn
                mn = diff

        powers = [2**i for i in range(19)]
        steps = 0
        while n:
            n = next_n(n)
            steps += 1
        return steps


# @lc code=end
