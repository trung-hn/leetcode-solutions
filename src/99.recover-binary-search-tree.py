#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# TAGS: Tree, DFS
# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time: O(NlogN). Space: O(N). Sorting
    def recoverTree(self, root: TreeNode) -> None:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        values = inorder(root)
        sorted_values = sorted(values)
        
        wanted_values = []
        for v1, v2 in zip(values, sorted_values):
            if v1 != v2:
                wanted_values.append(v1)
        
        def recover(node):
            if not node: return
            if node.val == wanted_values[0]:
                node.val = wanted_values[1]
            elif node.val == wanted_values[1]:
                node.val = wanted_values[0]
            recover(node.left)
            recover(node.right)
        recover(root)        
        
    # From article. Time and Space: O(N). Instead of sorting, we find 2 wanted values and switch them. 
    def recoverTree(self, root: TreeNode) -> None:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        values = inorder(root)
        
        # very clever way to find the 2 values. 
        # if they are next to each other, then we found them in the first if
        # if they are far away each other, then we choose v1 from first occurence and v2 from second occurence. (Because it is sorted.)
        x = y = None
        for v1, v2 in zip(values, values[1:]):
            if v1 > v2:
                y = v2
                if x is None:
                    x = v1
                else: break
                    
        def recover(node, x, y):
            if not node: return
            if node.val == x:
                node.val = y
            elif node.val == y:
                node.val = x
            recover(node.left, x, y)
            recover(node.right, x, y)
        recover(root, x, y)   
                
# @lc code=end

