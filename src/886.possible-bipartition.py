#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
# TAGS: Depth First Search
# REVIEWME: unconventional problem
class Solution:
    """
    Time and Space: O(N + E), E is number of dislikes
    """
    # 828 ms, 37.88%
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for start, end in dislikes:
            graph[start].append(end)
            graph[end].append(start)

        visited = {}
        def dfs(node, c = 0):
            if node in visited:
                return visited[node] == c
            visited[node] = c
            return all(dfs(child, c ^ 1) for child in graph[node])
        
        return all(dfs(i) for i in range(N) if i not in visited)
# @lc code=end

