#
# @lc app=leetcode id=785 lang=python3
#
# [785] Is Graph Bipartite?
#

# @lc code=start
# TAGS: BFS, DFS, Graph
class Solution:
    # 180 ms, 47.49%. Time and Space: O(E+V)
    def isBipartite(self, graph: List[List[int]]) -> bool:
        sets = [set(), set()]
        visited = set()
        for n in range(len(graph)):
            if any(n in s for s in sets): continue
            q = [(n, 0)]
            for node, set_index in q:
                if node in visited: continue
                visited.add(node)
                for nei in graph[node]:
                    if nei in sets[set_index]: return False
                    sets[1 - set_index].add(nei)
                    q.append((nei, not set_index))
        return True
# @lc code=end

