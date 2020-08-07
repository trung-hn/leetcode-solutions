#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# TAGS: Hash Table, Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 28 ms, 95.77%. Time: O(NlogN) because of sorting. Space: O(N) where N in the number of nodes.
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.nodes = collections.defaultdict(list)
        def dfs(node, x=0, y=0):
            if not node: return
            self.nodes[x].append((-y, node.val))
            dfs(node.left, x - 1, y - 1)
            dfs(node.right, x + 1, y - 1)
        dfs(root)

        ans = []
        for k in sorted(self.nodes.keys()):
            ans.append([val for y, val in sorted(self.nodes[k])])
        return ans
# @lc code=end

