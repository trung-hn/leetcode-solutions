#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
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
    # 56 ms, 23.54 %. Time and Space: O(N), O(N)
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node, depth=0, id_=1):
            if not node: return
            if depth >= len(depths):
                depths.append([float("inf"), - float("inf")])
            if depths[depth][0] > id_:
                depths[depth][0] = id_
            if depths[depth][1] < id_:
                depths[depth][1] = id_
            
            dfs(node.left, depth + 1, id_ * 2)
            dfs(node.right, depth + 1, id_ * 2 + 1)
        depths = []
        dfs(root)
        return max(hi - lo + 1 for lo, hi in depths)
# @lc code=end

