#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#

# @lc code=start
# TAGS: Tree, DFS, BFS, Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 36 ms, 56.44%. Time and Space: O(N)
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.ans = 0
        self.deepest = 0
        def dfs(node, depth=0):
            if not node: 
                self.deepest = max(self.deepest, depth)
                return depth
            
            left = dfs(node.left, depth + 1)
            right =  dfs(node.right, depth + 1)
            if left == right == self.deepest:
                self.ans = node
            return max(left, right)
        dfs(root)
        return self.ans
# @lc code=end

