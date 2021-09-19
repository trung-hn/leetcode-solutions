#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            return dfs(node.left) + dfs(node.right) + [node.val] if node else []
        return dfs(root)

    # Iteration
    # Time and Space: O(N)
    def postorderTraversal(self, root):
        stack = [(root, False)]
        ans = []
        while stack:
            node, visited = stack.pop()
            if node:
                if not visited:
                    stack.extend(
                        [(node, True), (node.right, False), (node.left, False)])
                else:
                    ans.append(node.val)
        return ans
# @lc code=end
