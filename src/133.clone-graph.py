#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
# TAGS: DFS, BFS, Graph
# REVIEWME: DFS, BFS, Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # 40 ms, 58.21%. Time: O(N+M). Space:O(N)
    def cloneGraph(self, node: 'Node') -> 'Node':
        def create_nodes(node, visited=set()):
            if not node: return
            if node.val in visited: return
            visited.add(node.val)
            
            nodes[node.val] = Node(node.val)
            for nei in node.neighbors:
                create_nodes(nei, visited)
        
        def connect_nodes(node, visited=set()):
            if not node: return
            if node.val in visited: return
            visited.add(node.val)
            
            for nei in node.neighbors:
                nodes[node.val].neighbors.append(nodes[nei.val])
                connect_nodes(nei, visited)
            
        nodes = {}
        create_nodes(node)
        connect_nodes(node)
        return nodes[node.val] if node else None

    # 36 ms, 81.02%. DFS similar to article but not returning node. Time: O(N+M). Space:O(N)
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = {}
        def dfs(node):
            if not node: return
            if node.val in self.visited: return

            curr = Node(node.val)
            self.visited[node.val] = curr
            for nei in node.neighbors:
                dfs(nei)
                curr.neighbors.append(self.visited[nei.val])

        dfs(node)
        return self.visited[1] if node else None

    # 28 ms, 98.79%. Time: O(N+M). Space:O(N)
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return 
        visited = {1:Node(node.val)}
        queue = [node]
        for node in queue:
            for nei in node.neighbors:
                if nei.val not in visited:
                    visited[nei.val] = Node(nei.val)
                    queue.append(nei)
                visited[node.val].neighbors.append(visited[nei.val])
        return visited[1]

# @lc code=end

