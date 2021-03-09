#
# @lc app=leetcode id=623 lang=python3
#
# [623] Add One Row to Tree
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
    # 56 ms, 64.46%. Time: O(N). Space: O(N)
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, root)

        def dfs(node, depth=2):
            if not node:
                return
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)
            if depth == d:
                node.left = TreeNode(v, left)
                node.right = TreeNode(v, None, right)
            return node
        return dfs(root)
# @lc code=end
