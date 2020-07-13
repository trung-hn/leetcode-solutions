#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# TAGS: Tree, Pythonic
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 48 ms, 13.67%
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            return p is q
            # same as:
            # if p==q: return True
            # else: return False
        return p.val==q.val and self.isSameTree(p.left,q.left) \
                            and self.isSameTree(p.right,q.right)
# @lc code=end

