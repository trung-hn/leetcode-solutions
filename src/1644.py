# TAGS: Premium, Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 320 ms, 53.31%. Time: O(N). Space: O(H)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(node, p, q):
            if not node: return False
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            curr = node.val in (p.val, q.val)
            if left + right + curr == 2:
                self.ans = node
            return left or right or curr
        dfs(root, p, q)
        return self.ans