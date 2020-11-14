#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
# TAGS: Tree, BFS, DFS
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    """
    There is a solution with O(1) Space
    """
    # 72 ms, 20%. Time and Space: O(N). 2 passes
    def connect(self, root: 'Node') -> 'Node':
        nodes = []
        q = [(root, 0)]
        for node, depth in q:
            if not node: continue
            if depth >= len(nodes):
                nodes.append([])
            nodes[depth].append(node)
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))
        for row in nodes:
            for n1, n2 in zip(row, row[1:]):
                n1.next = n2
        return root
    
    # 60 ms, 78%. Time and Space: O(N). 1 pass
    def connect(self, root: 'Node') -> 'Node':
        prev = prev_depth = None
        q = [(root, 0)]
        for node, depth in q:
            if not node: continue
            if prev and depth == prev_depth :
                prev.next = node
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))
            prev, prev_depth = node, depth
        
        return root
# @lc code=end

