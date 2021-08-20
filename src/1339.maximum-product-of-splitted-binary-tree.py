#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
#

# @lc code=start
# TAGS: Tree, DFS, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # 388 ms, 44.81%. Time and Space: O(N)
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def tree_sum(node):
            return node.val + tree_sum(node.left) + tree_sum(node.right) if node else 0

        self.total = tree_sum(root)
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            self.ans = max(self.ans, total * (self.total - total))
            return total

        dfs(root)
        return self.ans % (10 ** 9 + 7)

# @lc code=end
