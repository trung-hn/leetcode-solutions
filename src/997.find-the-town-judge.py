#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
# TAGS: Array, Hash Table, Graph
from typing import List


class Solution:
    # 1576 ms, 5.04%. Time: O(N*M). Space: O(1)
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        # Edge case
        if not trust and N == 1:
            return N

        for person in range(1, N + 1):  # O(N)
            out_trust = sum(a == person for a, _ in trust)  # O(M)
            in_trust = sum(b == person for _, b in trust)  # O(M)
            if out_trust == 0 and in_trust == N - 1:
                return person
        return -1

    # 1576 ms, 5.04%. Time: O(N + M). Space: O(N)
    def findJudge1(self, N: int, trust: List[List[int]]) -> int:

        trust_cnt = [0] * (N + 1)
        for a, b in trust:  # O(M)
            trust_cnt[a] -= 1
            trust_cnt[b] += 1
        for i in range(1, N + 1):  # O(N)
            if trust_cnt[i] == N - 1:
                return i
        return -1


# @lc code=end
