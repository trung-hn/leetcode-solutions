#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#

# @lc code=start
# TAGS: Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 56 ms, 13.23%. Time and Space: O(N)
    def isCompleteTree(self, root: TreeNode) -> bool:
        layers = []
        def dfs(node, depth=0, sofar=0):
            if not node: return
            if depth >= len(layers):
                layers.append([])
            layers[depth].append(sofar)
            dfs(node.left, depth + 1, sofar * 2)
            dfs(node.right, depth + 1, sofar * 2 + 1)
        dfs(root)
        deepest = len(layers)
        for d, layer in enumerate(layers):
            if len(layer) != 2**d and d != deepest - 1: return False
            if layer != list(range(len(layer))): return False
        return True
    
    # 32 ms, 84.73%. Time and Space: O(N)
    # Same as above but cleaner: we know that the last value has to = len(nodes)
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [(root, 1)]
        for node, v in nodes:
            if not node: continue
            nodes.append((node.left, v * 2))
            nodes.append((node.right, v * 2 + 1))
        return nodes[-1][1] == len(nodes)
            
# @lc code=end

