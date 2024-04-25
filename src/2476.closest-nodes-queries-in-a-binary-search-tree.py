#
# @lc app=leetcode id=2476 lang=python3
#
# [2476] Closest Nodes Queries in a Binary Search Tree
#


# @lc code=start
# TAGS: Array, Binary Search, Tree, Depth-First Search, Binary Search Tree, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from bisect import bisect


class Solution:
    # Time: O(NlogN). Space: O(N)
    def closestNodes(
        self, root: Optional[TreeNode], queries: List[int]
    ) -> List[List[int]]:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        nums = []
        inorder(root)
        ans = []
        for q in queries:
            i = bisect.bisect_left(nums, q)
            if i == len(nums):
                ans.append([nums[i - 1], -1])
            elif nums[i] == q:
                ans.append([q, q])
            elif i == 0:
                ans.append([-1, nums[i]])
            else:
                ans.append([nums[i - 1], nums[i]])
        return ans


# @lc code=end
