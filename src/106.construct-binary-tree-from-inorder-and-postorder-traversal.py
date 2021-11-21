#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# TAGS: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 292 ms, 20%. Time: O(NlogN)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {val: i for i, val in enumerate(postorder)}

        def recreate(l, r):
            if l == r:
                return None
            if l + 1 == r:
                return TreeNode(inorder[l])

            center = inorder.index(max(inorder[l:r], key=pos.get))
            return TreeNode(inorder[center], recreate(l, center), recreate(center + 1, r))
        return recreate(0, len(inorder))

    # 44 ms, 99.52%. Time and Space: O(N)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {val: i for i, val in enumerate(inorder)}

        def recreate(l, r):
            if l == r:
                return None
            if l + 1 == r:
                return TreeNode(postorder.pop())
            center = pos[postorder.pop()]
            right = recreate(center + 1, r)
            left = recreate(l, center)
            return TreeNode(inorder[center], left, right)
        return recreate(0, len(inorder))

# @lc code=end
