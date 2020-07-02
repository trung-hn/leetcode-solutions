#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# TAGS: Tree, Breath First Search
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    Time and Space: O(N), O(N)
    """
    
    # how to do it wihout reversed(ans)
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        q = [(root, 0)]
        depth = 0
        for node, depth in q:
            if node:
                if depth < len(ans):
                    ans[ - depth - 1].append(node.val)
                else:
                    ans.insert(0, [node.val])
                depth += 1
                q.append((node.left, depth))
                q.append((node.right, depth))
        return ans
    
    # 40 ms, 82%
    def levelOrderBottom1(self, root: TreeNode) -> List[List[int]]:
        ans = []
        q = [(root, 0)]
        depth = 0
        for node, depth in q:
            if node:
                if depth < len(ans):
                    ans[depth].append(node.val)
                else:
                    ans.append([node.val])
                depth += 1
                q.append((node.left, depth))
                q.append((node.right, depth))
        return reversed(ans)
                
# @lc code=end

