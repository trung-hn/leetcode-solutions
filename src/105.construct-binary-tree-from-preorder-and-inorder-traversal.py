#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# TAGS: Array, Tree, DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    # 1028 ms, 5%. Time: O(N^2). Space: O(N) Start from preorder
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_pos = {val: i for i, val in enumerate(inorder)}

        def dfs(preorder):
            if not preorder:
                return None
            parent = preorder[0]
            left_children = [val for val in preorder[1:]
                             if inorder_pos[val] < inorder_pos[parent]]
            right_children = [val for val in preorder[1:]
                              if inorder_pos[val] > inorder_pos[parent]]
            node = TreeNode(parent)
            node.left = dfs(left_children)
            node.right = dfs(right_children)
            return node
        return dfs(preorder)

    # 88 ms, 61.89%. Time: O(N). Space: O(N) Start from inorder
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inorder_pos = {val: i for i, val in enumerate(inorder)}
        self.ptr = 0

        def dfs(left, right):
            if left == right:
                return None

            # Root for Tree Node
            parent = preorder[self.ptr]
            self.ptr += 1
            node = TreeNode(parent)

            # Left and Right children
            node.left = dfs(left, inorder_pos[parent])
            node.right = dfs(inorder_pos[parent] + 1, right)
            return node
        return dfs(0, len(inorder))
# @lc code=end
