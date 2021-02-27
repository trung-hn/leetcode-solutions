#
# @lc app=leetcode id=802 lang=python3
#
# [802] Find Eventual Safe States
#

# @lc code=start
# TAGS: DFS, Graph
class Solution:  
    # 764 ms, 25.20%.
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = [None] * len(graph)
        for i, val in enumerate(graph):
            if val == []: safe_nodes[i] = True
                
        visited = set()
        def dfs(node):
            if safe_nodes[node]: return True
            if safe_nodes[node] == False: return False
            if node in visited: return False
            
            # Add current node to parent list
            visited.add(node)
            
            # Check if all nei leads to safe nodes
            is_safe = True
            for nei in graph[node]:
                is_safe = is_safe and dfs(nei)
            safe_nodes[node] = is_safe
            
            # Remove current node to parent list
            visited.remove(node)
            return is_safe
        
        for i in range(len(graph)):
            dfs(i)
                
        return [i for i, val in enumerate(safe_nodes) if val]

# @lc code=end

