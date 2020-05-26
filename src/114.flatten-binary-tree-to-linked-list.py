#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# TAGS: Tree, Depth First Search
class Solution:
    """
    Do not return anything, modify root in-place instead.
    There is a O(1) Space solution in the article (Morris Traversal)
    """
    # 36 ms, 96%
    def flatten(self, root: TreeNode) -> None:
        
        # dfs to get all values
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.extend([node.right, node.left])
        
        # make a tree out of those values
        for val in ans[1:]:
            root.right = TreeNode(val)
            root.left = None
            root = root.right
    
    def __init__(self):
        self.prev = None
    
    # Recursive from discussion. Time: O(N), Space: O(1)
    def flatten(self, root: TreeNode) -> None:
        if root:
            self.flatten(root.right)
            self.flatten(root.left)

            root.right = self.prev
            root.left = None
            self.prev = root
        
    # 32 ms, 90.55%. O(N) Time, O(N) Space because of stack
    # Although we create a node here, we don't actually return it. 
    # We only use it as a head to handle edge case.
    def flatten(self, root: TreeNode) -> None:
        head = prev = TreeNode(0)
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                if prev:
                    prev.right = node
                    node.left = None
                prev = prev.right
        
# @lc code=end

