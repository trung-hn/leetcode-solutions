#
# @lc app=leetcode id=1080 lang=python3
#
# [1080] Insufficient Nodes in Root to Leaf Paths
#

# @lc code=start
# TAGS: DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # 100 ms, 46.07%. Time and Space: O(N)
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node, sofar=0):
            # leaf node
            if not node:
                return None
            if node.left is node.right is None:
                sofar += node.val
                return node if sofar >= limit else None
            # dfs
            left = dfs(node.left, sofar + node.val)
            right = dfs(node.right, sofar + node.val)

            # Remove this node
            if left is right is None:
                return None
            node.left = left
            node.right = right
            return node
        return dfs(root)
# @lc code=end
