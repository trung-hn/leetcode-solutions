#
# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#


# @lc code=start
# TAGS: Dynamic Programming
# REVIEWME: Dynamic Programming
class Solution:
    # 277 ms. 60%.
    # Time: O(N * K). Space: O(K)
    def kInversePairs(self, n: int, k: int) -> int:
        """
        This Optimal Solution took me 1 hour from scratch.
        """
        # Realization: k increases by 1 everytime we shift left
        # 1 2 3 4 => k = 0
        # 1 2 4 3 => k = 1
        # 1 4 2 3 => k = 2
        # 4 1 2 3 => k = 3

        # let nk(i, j) be the collections of sequences where n = i, k = j
        # nk(5, 5) = nk(4, 5) + nk(4, 4) + nk(4, 3) + nk(4, 2) + nk(4, 1)
        # because
        # we put `5` at index 4 of sequences from nk(4, 5) => shift left 0 times => contains 5 + 0 = 5 pairs
        # we put `5` at index 3 of sequences from nk(4, 4) => shift left 1 times => contains 4 + 1 = 5 pairs
        # we put `5` at index 2 of sequences from nk(4, 3) => shift left 2 times => contains 3 + 2 = 5 pairs
        # we put `5` at index 1 of sequences from nk(4, 2) => shift left 3 times => contains 2 + 3 = 5 pairs
        # we put `5` at index 0 of sequences from nk(4, 1) => shift left 4 times => contains 1 + 4 = 5 pairs
        # we cannot put `5` at index < 0 => nk(4, 0) and below is not needed

        # Simulation:
        # n = 2: 1 1
        # n = 3: 1 2 2 1
        # n = 4: 1 3 5 6 5  3  1
        # n = 5: 1 4 9 15 20 22 20 15 9 4 1

        # DP Formula:
        # prev[0] = 1
        # for each n:
        #   cur[i] = sum(prev[j] for j in range(0, i + 1)). However, ignore values where j < i - n
        #   prev = cur

        MOD = 10**9 + 7
        prev = collections.defaultdict(int, {0: 1})
        for i in range(1, n):
            max_k = int(i * (i + 1) / 2)
            cur = collections.defaultdict(int, {0: 1, max_k: 1})
            for j in range(1, k + 1):
                cur[j] = (cur[j - 1] + prev[j]) % MOD
                if j > i:
                    cur[j] = (cur[j] - prev[j - i - 1]) % MOD
            prev = cur
        return prev[k]


# @lc code=end
