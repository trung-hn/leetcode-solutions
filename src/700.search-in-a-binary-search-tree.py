#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# TAGS: Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Time: O(H)
    Space: O(1)
    """
    # Recursive
    def searchBST(self, node: TreeNode, val: int) -> TreeNode:
        def dfs(node):
            if node:
                if node.val == val:
                    return node
                if node.val > val:
                    return dfs(node.left)
                if node.val < val:
                    return dfs(node.right)
        return dfs(node)
    
    # Iterative.
    def searchBST(self, node: TreeNode, val: int) -> TreeNode:
        stack=[node]
        for node in stack:
            if node:
                if node.val==val:
                    return node
                elif node.val<val:
                    stack.append(node.right)
                elif node.val>val:
                    stack.append(node.left)
        return None
# @lc code=end

