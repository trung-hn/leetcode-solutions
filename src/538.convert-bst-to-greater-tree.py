#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#

# @lc code=start
# TAGS: Tree, BFS, DFS, Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 92 ms, 16%
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            return dfs(node.right) + [node.val] + dfs(node.left) if node else []
        
        L = dfs(root)
        L = list(itertools.accumulate(L, lambda x,y:x+y))
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if not visited:
                    stack.extend([(node.right, False), (node, True), (node.left, False)])
                else:
                    node.val = L.pop()
        return root
    
    # 68 ms, 99%. Interative dfs
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    node.val += total
                    total = node.val
                else:
                    stack.extend([(node.left, False), (node, True), (node.right, False)])
        return root
    
    # Time: O(N). Space: O(H) Pythonic solution
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0
        def dfs(node):
            if not node: return
            dfs(node.right)
            node.val += self.total
            self.total = node.val
            dfs(node.left)
        dfs(root)
        return root
# @lc code=end

