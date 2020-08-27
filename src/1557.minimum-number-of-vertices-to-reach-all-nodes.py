#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#

# @lc code=start
# TAGS: Graph
import collections
import itertools
class Solution:
    # 1288 ms, 81.78 %. Time: O(V+E). Space: O(E)
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for f, t in edges:
            graph[f].append(t)
        
        tos = set(item for val in graph.values() for item in val)
        froms = set(graph.keys())
        return froms - tos

# @lc code=end

