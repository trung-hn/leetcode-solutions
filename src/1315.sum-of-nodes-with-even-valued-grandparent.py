#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#

# @lc code=start
# TAGS: Tree, DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # BFS
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = [(root, 0, 0)]
        ans = 0
        for node, parent, grand in q:
            if node:
                if grand:
                    ans += node.val
                q.append((node.left, node.val % 2 == 0, parent))
                q.append((node.right, node.val % 2 == 0, parent))
        return ans

    # 92 ms, 95.04%. DFS. Time: O(N). Space: O(N)
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, is_even_gp=None, is_even_p=None):
            if not node:
                return 0
            is_even = node.val % 2 == 0
            left = dfs(node.left, is_even_p, is_even)
            right = dfs(node.right, is_even_p, is_even)
            rv = node.val if is_even_gp else 0
            return left + right + rv
        return dfs(root)

# @lc code=end
