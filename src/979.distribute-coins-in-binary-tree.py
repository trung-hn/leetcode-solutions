#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#

# @lc code=start
# TAGS: Tree, DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 28 ms, 97%. O(N)
    def distributeCoins(self, root: TreeNode) -> int:
        self.rv = 0
        def dfs(node):
            if not node: return 0            
            left = dfs(node.left)
            right = dfs(node.right)
            val = left + right + node.val
            self.rv += abs(val - 1)
            return val - 1
        dfs(root)
        return self.rv

    # 28 ms, 97%. O(N). Same logic.
    # The idea is to move coins from parent to child no matter 
    # even if it has coins or not. (result in negative numbers).
    # Negative number means future coin will take that path.
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans += abs(left) + abs(right)
            total = node.val + left + right
            return total - 1
        dfs(root)
        return self.ans
# @lc code=end

