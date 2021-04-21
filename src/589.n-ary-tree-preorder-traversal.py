#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
# TAGS: Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    # Time and Space: O(N)
    def preorder(self, root: 'Node') -> List[int]:
        stack = [root]
        lst = []
        while(stack):
            node = stack.pop()
            if node:
                lst.append(node.val)
                for child in reversed(node.children):
                    stack.append(child)
        return lst

    # recursive, slightlt different
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        rv = [root.val]
        for c in root.children:
            rv += self.preorder(c)
        return rv

    # recursive
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        lst = []

        def dfs(node):
            if node:
                lst.append(node.val)
                for child in node.children:
                    dfs(child)
        dfs(root)
        return lst
# @lc code=end
