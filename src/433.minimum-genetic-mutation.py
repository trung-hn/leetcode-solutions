#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
# TAGS: Hash Table, String, BFS
import collections
from typing import List


class Solution:
    # Time: O(V+E). Space: O(V+E).
    # Important: note that a new visited is not needed for every BFS layer
    # Because that's the definition of BFS
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        neis = collections.defaultdict(list)
        bank.append(start)
        for g1 in bank:
            for g2 in bank:
                if g1 == g2:
                    continue
                diff = sum(c1 != c2 for c1, c2 in zip(g1, g2))
                if diff == 1:
                    neis[g1].append(g2)
                    neis[g2].append(g1)

        visited = set()
        q = [(start, 0)]
        for node, depth in q:
            if node == end:
                return depth
            for nei in neis[node]:
                if nei in visited:
                    continue
                visited.add(nei)
                q.append((nei, depth + 1))

        return -1


# @lc code=end
