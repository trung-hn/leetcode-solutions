#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# TAGS: Tree, BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # 32 ms, 80.03%. Time: O(N). Space: O(N)
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        depth = 0
        q = [(root, depth)]
        for node, depth in q:
            if node:
                if depth >= len(ans):
                    ans.append([])
                ans[depth].append(node.val)
                q.append((node.left, depth + 1))
                q.append((node.right, depth + 1))
        return ans
# @lc code=end
