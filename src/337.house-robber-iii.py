#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#

# @lc code=start
# TAGS: Dynamic Programming, Tree, DFS
import functools
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # LTE without memo. Time and Space: O(2^N). 
    # 60 ms, 20.85%. With memo Time and Space: O(N)
    def rob(self, root: TreeNode) -> int:
        @functools.lru_cache(None)
        def dfs(node, rob_prev=False):
            if not node: return 0
            rob = 0
            notrob = dfs(node.left, False) + dfs(node.right, False)
            if not rob_prev:
                rob = dfs(node.left, True) + dfs(node.right, True) + node.val
            return max(notrob, rob)
        return dfs(root)

    # 48 ms, 70.13%. Normal recursion. From discussion. 
    # Time: O(N). Space: O(H)
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node: return 0, 0
            left, right = dfs(node.left), dfs(node.right)
            now = left[1] + right[1] + node.val
            later = max(left) + max(right)
            return (now, later)
        return max(dfs(root))

# @lc code=end

