#
# @lc app=leetcode id=847 lang=python3
#
# [847] Shortest Path Visiting All Nodes
#

# @lc code=start
# TAGS: Dynamic Programming, Bit Manipulation, BFS, Graph Bitmask
# REVIEWME: Bit Manipulation, Graph Bitmask
from typing import List


class Solution:
    # dfs with memo. 696 ms, 31.56%.
    # Time: O(2^N * N^2). Space: O(2^N * N)
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        def dp(node, mask):
            state = (node, mask)
            if state in cache:
                return cache[state]
            if mask & (mask - 1) == 0:
                return 0
            cache[state] = float("inf")
            for nei in graph[node]:
                if mask & (1 << nei):
                    already_visited = 1 + dp(nei, mask)
                    not_visited = 1 + dp(nei, mask ^ (1 << node))
                    cache[state] = min(
                        cache[state], already_visited, not_visited)
            return cache[state]

        N = len(graph)
        cache = {}
        mask = (1 << N) - 1
        return min(dp(node, mask) for node in range(N))

    # BFS with memo. 384 ms, 46.65%
    # Time: O(2^N * N^2). Space: O(2^N * N)
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        steps = 0
        memo = set()
        N = len(graph)
        final_state = (1 << N) - 1
        q = [(i, 1 << i) for i in range(N)]
        while 1:
            new = []
            for node, state in q:
                if state == final_state:
                    return steps
                for nei in graph[node]:
                    if (nei, state | 1 << nei) in memo:
                        continue
                    new.append((nei, state | 1 << nei))
                    memo.add((nei, state | 1 << nei))
            q = new
            steps += 1

# @lc code=end
