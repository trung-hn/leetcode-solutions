#
# @lc app=leetcode id=1457 lang=python3
#
# [1457] Pseudo-Palindromic Paths in a Binary Tree
#

# @lc code=start
# TAGS: Bit Manipulation, Tree, Depth First Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 412 ms, 85.09%. Time: O(N). Space: O(H)
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:      
        def dfs(node, evens=[True]*10):
            if not node: return
            evens[node.val] ^= 1 # Flip bit
            
            if node.left is node.right is None:
                if evens.count(False) < 2:
                    self.ans += 1
            
            dfs(node.left, evens)
            dfs(node.right, evens)
            evens[node.val] ^= 1 # Flip bit
        self.ans = 0
        dfs(root)
        return self.ans

# @lc code=end

