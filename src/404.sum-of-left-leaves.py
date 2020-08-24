#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#

# @lc code=start
# TAGS: Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 36 ms, 60.61%. Time O(N), Space: O(H)
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node, left_leave=False):
            if not node: return 0
            if node.left is node.right is None and left_leave: 
                return node.val
            return dfs(node.left, left_leave=True) + dfs(node.right)
        return dfs(root)
# @lc code=end

