# TAGS: Premium, Tree, BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 488 ms, 5.04%. Time and Space: O(N)
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if u == root: return None
        
        queue = [(root, 0)]
        values = []
        for node, depth in queue:
            if not node: continue
            if depth > len(values) - 1:
                values.append([])
            values[depth].append(node)
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
    
        for row in values:
            for v1, v2 in zip(row, row[1:]):
                if v1 == u:
                    return v2
        return None
    # 316 ms, 78.66%. Similar to above but more optimized. 
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        queue = [(root, 0)]
        found_depth = -1
        for node, depth in queue:
            if not node: continue
            if found_depth >= 0:
                if depth == found_depth: 
                    return node
                return None
            
            if node == u: found_depth = depth
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
