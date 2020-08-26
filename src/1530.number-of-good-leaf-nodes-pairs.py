#
# @lc app=leetcode id=1530 lang=python3
#
# [1530] Number of Good Leaf Nodes Pairs
#

# @lc code=start
# TAGS: Tree, Depth First Search
# REVIEWME: Unusual Problem. 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect
class Solution:
    # 108 ms, 99.68 %. Time: O(N^2 LogN). Space: O(N)
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.cnt = 0        
        def count_pairs(left, right, depth): # O(NlogN)
            left.sort()
            right.sort()
            cnt = 0
            for val in left:
                if val - depth >= distance: break
                index = bisect.bisect_right(right, distance - val + 2*depth)
                cnt += index
            return cnt

        def dfs(node, depth=0):
            if not node: return []
            if node.left is node.right is None:
                return [depth]
            
            left_leaves = []
            if node.left:
                left_leaves = dfs(node.left, depth + 1)

            right_leaves = []
            if node.right:
                right_leaves = dfs(node.right, depth + 1)

            self.cnt += count_pairs(left_leaves, right_leaves, depth)
            return left_leaves + right_leaves

        dfs(root)
        return self.cnt

# @lc code=end

