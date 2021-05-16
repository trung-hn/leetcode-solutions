#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#

# @lc code=start
# TAGS: Greedy, Tree, Dynamic Programming, DFS
# REVIEW: Greedy, Tree, Dynamic Programming, DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            # 0: Strict ST; All nodes below this are covered, but not this one
            # 1: Normal ST; All nodes below and incl this are covered - no camera
            # 2: Placed camera; All nodes below this are covered, plus camera here

            if not node:
                return 0, 0, float('inf')
            L = dfs(node.left)
            R = dfs(node.right)

            # No camera on left or right node.
            dp0 = L[1] + R[1]

            # No camera on current node because camera is on either left or right node
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))

            # Put camera on current node.
            dp2 = 1 + min(L) + min(R)

            return dp0, dp1, dp2

        return min(dfs(root)[1:])

    # 44 s, 66.74%. Fill in node from bottom up greedily
    def minCameraCover(self, root: TreeNode) -> int:
        self.cnt = 0
        covered = {None}

        def dfs(node, par=None):
            if not node:
                return
            dfs(node.left, node)
            dfs(node.right, node)

            # Is it root node and not cover
            if par is None and node not in covered:
                self.cnt += 1
                covered.update({par, node, node.left, node.right})

            # If children are not cover
            if not (node.left in covered and node.right in covered):
                self.cnt += 1
                covered.update({par, node, node.left, node.right})
        dfs(root)
        return self.cnt
# @lc code=end
