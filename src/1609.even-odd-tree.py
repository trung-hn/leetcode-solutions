#
# @lc app=leetcode id=1609 lang=python3
#
# [1609] Even Odd Tree
#

# @lc code=start
# TAGS: Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 788 ms, 9.28%. Time: O(N). Space: O(N)
    def isEvenOddTree(self, root: TreeNode) -> bool:
        values = []
        q = [(root, 0)]
        for node, depth in q:
            if not node: continue
            if depth >= len(values):
                values.append([])
            values[depth].append(node.val)
            q.append((node.left, depth + 1))
            q.append((node.right, depth + 1))
        
        for i, row in enumerate(values):
            if i % 2:
                if any(val % 2 for val in row):
                    return False
                if any(v1 <= v2 for v1, v2 in zip(row, row[1:])):
                    return False
            else:
                if any(val % 2 == 0 for val in row):
                    return False
                if any(v1 >= v2 for v1, v2 in zip(row, row[1:])):
                    return False 
        return True
    # 468 ms 93.14%. Time: O(N). Space: O(N). Pythonic 1 pass
    def isEvenOddTree(self, root: TreeNode) -> bool:
        even = True
        q = collections.deque([root])
        while q:
            prev = None
            for _ in range(len(q)):
                node = q.popleft()
                if not node: continue
                if even:
                    if node.val % 2 == 0: return False
                    if prev and node.val <= prev.val: return False
                else:
                    if node.val % 2 == 1: return False
                    if prev and node.val >= prev.val: return False
                q.append(node.left)
                q.append(node.right)
                prev = node
            even = not even
        return True

# @lc code=end

