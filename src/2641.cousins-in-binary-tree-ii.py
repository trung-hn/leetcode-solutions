#
# @lc app=leetcode id=2641 lang=python3
#
# [2641] Cousins in Binary Tree II
#


# @lc code=start
# TAGS: Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def get_total(node, depth=0):
            total_by_depth[depth] += node.val
            if node.left:
                get_total(node.left, depth + 1)
            if node.right:
                get_total(node.right, depth + 1)

        def dfs(node, depth=0, sibling=0):
            if not node:
                return
            total = 0
            if node.left:
                total += node.left.val
            if node.right:
                total += node.right.val
            dfs(node.left, depth + 1, total)
            dfs(node.right, depth + 1, total)
            node.val = total_by_depth[depth] - sibling

        total_by_depth = collections.defaultdict(int)
        get_total(root)
        dfs(root, 0, root.val)
        return root


# @lc code=end
