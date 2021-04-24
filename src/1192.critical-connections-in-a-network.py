#
# @lc app=leetcode id=1192 lang=python3
#
# [1192] Critical Connections in a Network
#

# @lc code=start
# TAGS: DFS
# REVIEWME: DFS, New Algorithm, Tarjan


class Solution:
    """
    Approach:
    Intuition: An edge is a critical connection, if and only if it is not in a cycle
    Tarjan Algo: Split graph into cycled group. the connections between them are critical connections

    DFS through all nodeds, find if it belong to a cycle, if it is not => critical connection
    """
    # 2236 ms, 81.10%. Time and Space: O(|E| + |V|)

    def criticalConnections(self, n, connections):
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ids = [-1] * n
        low = [-1] * n
        self.cnt = 0

        critical_connections = []

        def dfs(node, parent=None):
            # First visit
            visited[node] = True
            # Set to current counter
            ids[node] = low[node] = self.cnt
            # Increase Counter
            self.cnt += 1

            for nei in graph[node]:
                if nei == parent:
                    continue
                if not visited[nei]:
                    dfs(nei, node)

                # Find the quickest way to get to current node.
                low[node] = min(low[node], low[nei])

                # If this quickest way is the current way (no cycle) => critical
                if low[nei] > ids[node]:
                    critical_connections.append([node, nei])

        dfs(0)
        return critical_connections
# @lc code=end
