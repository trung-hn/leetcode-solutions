#
# @lc app=leetcode id=2583 lang=python3
#
# [2583] Kth Largest Sum in a Binary Tree
#


# @lc code=start
# TAGS: Tree, Breadth-First Search, Sorting, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(NlogN). Space: O(N)
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, depth=0):
            if not node:
                return
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
            total[depth] += node.val

        total = collections.defaultdict(int)
        dfs(root)
        vals = sorted(total.values(), reverse=True)
        return -1 if k > len(vals) else vals[k - 1]


# @lc code=end
