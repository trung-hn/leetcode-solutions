#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
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
    # 112 ms, 98%
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return None
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val) if root.left else TreeNode(val)
        elif val > root.val:
            root.right = self.insertIntoBST(root.right, val) if root.right else TreeNode(val)
        return root
    
    # Similar to above. 
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)
        if val < root.val: root.left = self.insertIntoBST(root.left, val)
        else: root.right = self.insertIntoBST(root.right, val)
        return root
    
    # 124 ms, 99.42%. Similar but Interative solution    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        node = root
        prev = None
        while node:
            prev = node
            node = node.left if node.val > val else node.right
        if prev.val > val: prev.left = TreeNode(val)
        else: prev.right = TreeNode(val)
        return root
# @lc code=end

