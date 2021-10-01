#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#

# @lc code=start
# TAGS: BFS, DFS, Graph


class Solution:
    # 2108 ms, 47.91%. Time and Space: O(N)
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:

        def dfs(node, visited):
            if node == end:
                return True

            visited[node] = 1
            for nei in neis[node]:
                if visited[nei] == 0 and dfs(nei, visited):
                    return True
            return False

        neis = collections.defaultdict(list)
        for s, e in edges:
            neis[s].append(e)
            neis[e].append(s)
        visited = [0] * n
        return dfs(start, visited)
# @lc code=end
