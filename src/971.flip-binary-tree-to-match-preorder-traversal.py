#
# @lc app=leetcode id=971 lang=python3
#
# [971] Flip Binary Tree To Match Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# TAGS: Tree, DFS
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # 24 ms, 100%. Time and Space: O(N)
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def dfs(node):
            if not node:
                return
            if voyage[self.i] != node.val:
                flip.append(-1)
            self.i += 1

            # flip
            if node.left and node.left.val != voyage[self.i]:
                flip.append(node.val)
                dfs(node.right)
                dfs(node.left)
            # not flip
            else:
                dfs(node.left)
                dfs(node.right)
        self.i = 0
        flip = []
        dfs(root)
        return [-1] if -1 in flip else flip
# @lc code=end
