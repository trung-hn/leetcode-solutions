#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# TAGS: Stack, Tree, DFS, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # Recursion.
    # Time and Space: O(N)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node):
            return dfs(node.left) + [node.val] + dfs(node.right) if node else []
        return dfs(root)

    # Iteration
    # Time and Space: O(N)
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        stack = [(root, False)]
        ans = []
        while stack:
            node, visited = stack.pop()
            if node:
                if not visited:
                    stack.extend(
                        [(node.right, False), (node, True), (node.left, False)])
                else:
                    ans.append(node.val)
        return ans
# @lc code=end
