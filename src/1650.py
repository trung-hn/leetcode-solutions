# TAGS: Premium, Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    # 76 ms, 18.62%. Time and Space: O(H)
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        while q:
            visited.add(q.val)
            q = q.parent
        
        while p:
            if p.val in visited: return p
            visited.add(p.val)
            p = p.parent
        return None
    
    # 92ms, 6.48%. Time and Space: O(H)
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def trace_parent(node, visited):
            if not node: return 
            if node.val in visited: return node
            visited.add(node.val)
            return trace_parent(node.parent, visited)
        
        visited = set()
        trace_parent(p, visited)
        return trace_parent(q, visited)
    
    # Brilliant solution from discussion for O(1) Space:
    # Notice that we go to the end the node when we reach the end. 
    # This will ensure both travel the same amount of nodes and thus, arrive at the intersection
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1