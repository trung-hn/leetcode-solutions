#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TAGS: Tree, Depth First Search
class Solution:
    """
    260 ms, 94.74%. 
    Time: O(N)
    Space: O(H)
    There is a 1 liner version by combining the condition in the summation.
    """
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, largest=-10001):
            if not node: return 0
            if node.val >= largest:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)
            return dfs(node.left, largest) + dfs(node.right, largest)
        return dfs(root)
# @lc code=end

