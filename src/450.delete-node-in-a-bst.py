#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# TAGS: Binary Search Tree, 2 ways
# REVIEWME: 
class Solution:
    # 112 ms, 9.9%. Time and Space O(H)
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        def get_max(node: TreeNode) -> int:
            while node and node.right:
                node = node.right
            return node.val
        
        def pop_max(node: TreeNode) -> None:
            if not node: return None
            if node.right:
                node.right = pop_max(node.right)
            else:
                return node.left
            return node
        
        def delete(node, value) -> TreeNode:
            if not node: return None
            if value > node.val:
                node.right = delete(node.right, value)
            elif value < node.val:
                node.left = delete(node.left, value)
            else:
                if node.left and node.right:
                    node.val = get_max(node.left)
                    node.left = pop_max(node.left)
                else:
                    return node.left or node.right
            return node
        return delete(root, key)
    
    # 96 ms, 12.42%. Time and Space O(H)
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        def get_max_left(node: TreeNode) -> int:
            node = node.left
            while node and node.right:
                node = node.right
            return node.val
        
        def get_min_right(node: TreeNode) -> None:
            node = node.right
            while node and node.left:
                node = node.left
            return node.val
        
        def delete(node, value) -> TreeNode:
            if not node: return None
            if value > node.val:
                node.right = delete(node.right, value)
            elif value < node.val:
                node.left = delete(node.left, value)
            else:
                if node.left is node.right is None:
                    return None
                if node.left:
                    node.val = get_max_left(node)
                    node.left = delete(node.left, node.val)
                else:
                    node.val = get_min_right(node)
                    node.right = delete(node.right, node.val)
            return node
        return delete(root, key)
        
# @lc code=end

