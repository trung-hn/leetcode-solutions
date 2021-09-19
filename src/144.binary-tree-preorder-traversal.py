#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# TAGS: Stack, Tree, DFS, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # Recursion.
    # Time and Space: O(N)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            return [node.val] + dfs(node.left) + dfs(node.right) if node else []
        return dfs(root)

    # Iteration.
    # Time and Space: O(N)
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [(root, False)]
        ans = []
        while stack:
            node, visited = stack.pop()
            if node:
                if not visited:
                    stack.extend(
                        [(node.right, False), (node.left, False), (node, True)])
                else:
                    ans.append(node.val)
        return ans
# @lc code=end
