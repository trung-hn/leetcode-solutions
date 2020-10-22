#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# TAGS: Tree, DFS, BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Both solutions are the same. Time: O(N). Space: O(H)
    """
    def minDepth(self, node: TreeNode) -> int:
        if node is None: return 0
        if node.left is None or node.right is None:
            return  1 + self.minDepth(node.left) + self.minDepth(node.right)
        return 1 + min(self.minDepth(node.left),self.minDepth(node.right))
    
    def minDepth(self, node: TreeNode) -> int:
        def dfs(node):
            if not node: return 0
            left, right = dfs(node.left), dfs(node.right)
            if node.left and node.right:
                return min(left, right) + 1
            return left + right + 1
        return dfs(node)
# @lc code=end

