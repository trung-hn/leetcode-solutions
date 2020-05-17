#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TAGS: trees, recursion
# REVIEWME:
class Solution:
    # 24 ms, 97.22%. Time: O(N). Space: O(H)
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.rv = False
        def tree_traversal(root, depth=0):
            if not root: return 0
            if root.val == x or root.val == y: return depth
            left = tree_traversal(root.left, depth + 1)
            right = tree_traversal(root.right, depth + 1)

            # Check if depth are equals and not direct children
            if left == right and left > depth + 1:
                self.rv = True
            
            # Return max child
            return max(left, right)
        tree_traversal(root)
        return self.rv

# @lc code=end

