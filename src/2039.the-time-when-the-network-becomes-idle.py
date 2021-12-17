#
# @lc app=leetcode id=2039 lang=python3
#
# [2039] The Time When the Network Becomes Idle
#

# @lc code=start
# TAGS: Array, BFS, Graph
from collections import defaultdict
from typing import List


class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:

        def get_operating_duration(dist, pat):
            shutoff_time = 2 * dist
            last_msg_time = ((shutoff_time - 1) // pat) * pat
            return shutoff_time + last_msg_time

        neis = defaultdict(list)
        for a, b in edges:
            neis[a].append(b)
            neis[b].append(a)

        # BFS to find shortest_path
        q = [(0, 0)]
        shortest = {}
        for node, dist in q:
            if node in shortest:
                continue
            shortest[node] = dist
            for nei in neis[node]:
                q.append((nei, dist + 1))

        # Find longest operating time
        rv = 0
        for node, dist in shortest.items():
            if node == 0:
                continue
            rv = max(rv, get_operating_duration(dist, patience[node]))
        return rv + 1
# @lc code=end
