#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#

# @lc code=start
# TAGS: Tree, DFS, 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     40 ms, 60.44%. Time: O(N). Space: O(H)
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, min_parent, max_parent):
            if not node: return 
            self.ans = max([self.ans, abs(node.val - min_parent), abs(node.val - max_parent)])
            
            min_parent = min(min_parent, node.val)
            max_parent = max(max_parent, node.val)
            dfs(node.left, min_parent, max_parent)
            dfs(node.right, min_parent, max_parent)
            
        dfs(root, root.val, root.val)
        return self.ans
# @lc code=end

