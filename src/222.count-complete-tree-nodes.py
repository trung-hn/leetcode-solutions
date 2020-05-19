#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# TAGS: Binary Search, Tree
# REVIEWME:
class Solution:
    """
    There are 3 solutions in this file
    1. O(N) using queue
    2. O(logN logN) using nested Binary search
    2. O(logN logN) using nested Binary search (Optimal)
    """

    # 204 ms, 5.19% O(N)
    def countNodes(self, root: TreeNode) -> int:
        count = 0
        queue = [root]
        for node in queue:
            if node:
                count += 1
                queue.extend([node.right, node. left])
        return count
    
    # 128 ms, 6.04% O(logN logN) but slow because of the str operation
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        D = 0
        node = root
        while node:
            node = node.left
            D += 1
        
        # binary_search
        lo, hi = 0, 2**(D-1)-1
        while lo < hi:
            mid = (lo + hi)//2
            rv = self.binary_search(root, mid, D)
            if rv == -1:
                lo = mid + 1
            elif rv == 1:
                hi = mid
            elif rv == 0:
                lo = mid
                break
        return sum(2**d for d in range(D-1)) + lo + 1
    
    # binary_search the tree
    def binary_search(self, root, number, depth):
        mem1 = root
        mem2 = number
        number = format(number, f'0{depth-1}b')
        for digit in number[:-1]:
            root = root.left if digit == '0' else root.right
        if number[-1] == '0' and not root.left: return 1 # next node is not available
        if number[-1] == '1' and not root.right: return 1 # next node is not available
        if number[-1] == '0' and not root.right: return 0 # right node
        if number[-1] == '1' and root.right and self.binary_search(mem1, mem2+1, depth) == 1: return 0 # right node
        return -1
    
    # 64 ms, 99% best and most pythonic. O(logN logN)
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        right_depth = self.get_depth(root.right)
        left_depth = self.get_depth(root.left)
        if right_depth == left_depth:
            return 2**left_depth + self.countNodes(root.right)
        else:
            return 2**right_depth + self.countNodes(root.left)
        
    def get_depth(self, node):
        if not node: return 0
        return 1 + self.get_depth(node.left)
# @lc code=end

