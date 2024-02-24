#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
# TAGS: Dynamic Programming, Heap, Breadth First Search:
# REVIEWME:  Dijkstra's Algorithm, Graph
import collections
from typing import List
import heapq


class Solution:
    """
    # Idea: Use a min heap to find the fatest way to get to node (not cheapest)
    """

    # 98 ms, 64.80%.
    # Time: O((E+V)*log(E+V)). Space: O(N*K)
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        fs = collections.defaultdict(list)
        for s, d, p in flights:
            fs[s].append((d, p))

        visited = collections.defaultdict(lambda: float("inf"))
        heap = [(0, 0, src)]
        while heap:
            stops, cost, curr = heapq.heappop(heap)

            # Optimal solution found for `curr` already
            if curr in visited and visited[curr] <= cost:
                continue
            visited[curr] = min(visited[curr], cost)

            if stops > k:
                continue
            for d, p in fs[curr]:
                heapq.heappush(heap, (stops + 1, cost + p, d))

        return visited.get(dst, -1)


# @lc code=end
