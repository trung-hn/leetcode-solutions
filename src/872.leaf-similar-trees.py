#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# REVIEWME: Iterator
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 28 ms, 99%
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def get_leaf(node):
            if node:
                if node.left is node.right is None:
                    yield node.val
                else:
                    yield from get_leaf(node.left)
                    yield from get_leaf(node.right)

        return list(get_leaf(root1)) == list(get_leaf(root2))


# @lc code=end
