#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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
    # 104 ms, 5.83%. In order traversal. General formula
    # Time: O(H + k), Space: O(H + k)
    def kthSmallest(self, node: TreeNode, k: int) -> int:
        cnt = 0
        stack = [(node, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    cnt += 1
                    if cnt == k:
                        return node.val
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))

    # 104 ms, 5.83%. In order traversal. Optimal formula
    # Time: O(H + k), Space: O(H + k)
    def kthSmallest(self, node: TreeNode, k: int) -> int:
        stack=[]
        counter=0
        while(stack or node):
            while(node):
                stack.append(node)
                node=node.left
            node=stack.pop()
            counter+=1
            if counter==k:
                return node.val
            node=node.right
# @lc code=end

