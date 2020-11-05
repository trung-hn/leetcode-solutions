#
# @lc app=leetcode id=310 lang=python3
#
# [310] Minimum Height Trees
#

# @lc code=start
# TAGS: BFS, Graph
# REVIEWME: BFS, Graph, Topology Sorting
class Solution:
    # LTE. Time: O(V*E). Space: O(E)
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
            
        def get_height(node, parent=-1):
            height = 0
            for next_node in graph[node]:
                if next_node == parent: continue
                height = max(height, get_height(next_node, node))
            return height + 1
        
        ans = []
        min_height = float('inf')
        for i in range(n):
            height = get_height(i)
            if height > min_height: continue
            elif height < min_height:
                ans = []
                min_height = height
            ans.append(i)
        return ans
        
    # 228 ms, 90.87%. Time and Space: O(V)
    # From article. topology sorting. trim 1 layer of leaves at a time
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n < 2:
            return list(range(n))
        graph = collections.defaultdict(set)
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
        
        leaves = []
        for v, e in graph.items():
            if len(e) == 1:
                leaves.append(v)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    graph[neighbor].discard(leaf)
                    if len(graph[neighbor]) == 1:
                        new_leaves.append(neighbor)
            
            leaves = new_leaves
        return leaves
            
# @lc code=end

