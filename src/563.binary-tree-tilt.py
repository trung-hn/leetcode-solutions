#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#

# @lc code=start
# TAGS: Tree, DFS, Recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 56 ms, 72.34%. Time: O(N). Space: O(H)
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans += abs(left - right)
            return left + right + node.val
        dfs(root)
        return self.ans
# @lc code=end

