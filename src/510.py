"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

# TAGS: Premium, Tree
class Solution:

    # Time: O(H). Space: O(H)
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        def dfs_right_child(node):
            return dfs_right_child(node.left) if node.left else node
        
        def dfs_parent(node, child_val):
            if not node: return None
            if node.left and node.left.val == child_val:
                return node
            return dfs_parent(node.parent, node.val)
            
        # Right child exists
        if node.right:
            return dfs_right_child(node.right)
        return dfs_parent(node.parent, node.val)

    # Cleaner solution. Time: O(H). Space: O(1)
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # the successor is somewhere lower in the right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # the successor is somewhere upper in the tree
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent
