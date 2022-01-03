#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
# TAGS: Array, Hash Table, Graph
from typing import List


class Solution:
    # 805 ms, 20.73%. Time and Space: O(N)
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_freq = [0] * (N + 1)
        for a, b in trust:
            trust_freq[a] -= 1
            trust_freq[b] += 1
        judge = [i for i, val in enumerate(trust_freq) if val == N - 1]
        return judge.pop() if judge else - 1
# @lc code=end
