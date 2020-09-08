#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# TAGS: Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 36 ms, 96%. Time: O(N), N is number of node. Space: O(N) because of queue
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = []
        q = [(root, "")]
        for node, sofar in q:
            if node:
                sofar += str(node.val)
                if node.left is node.right is None:
                    ans.append(sofar)
                q.extend([(node.left, sofar), (node.right, sofar)])
        return sum(map(lambda x: int(x,2), ans))
    
    # 32 ms, 98%. Cleaner. Time O(N). Space O(H)
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, val=0):
            if not node: return 0
            val = val*2 + node.val # Pay attention to the order of binary numbers
            if node.left is node.right is None:
                return val
            return dfs(node.left, val) + dfs(node.right, val)
        return dfs(root)
# @lc code=end

