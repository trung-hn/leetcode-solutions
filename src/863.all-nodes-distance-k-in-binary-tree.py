#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#

# @lc code=start
# TAGS: Tree, BFS, DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 36 ms, 72.59%. Time and Space: O(N)
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def get_nodes(node, k):
            if not node or k < 0: return
            if k == 0:
                self.nodes.append(node.val)
                return
            get_nodes(node.left, k - 1)
            get_nodes(node.right, k - 1)
        
        def dfs(node):
            if not node: return False, 0
            
            if node.val == target.val:
                get_nodes(node, K)
                return True, 1
            
            is_target, d = dfs(node.left)
            if is_target:
                if d == K: self.nodes.append(node.val)
                else: get_nodes(node.right, K - d - 1)
                return True, d + 1
                
            is_target, d = dfs(node.right)
            if is_target:
                if d == K: self.nodes.append(node.val)
                else: get_nodes(node.left, K - d - 1)
                return True, d + 1
            return False, 0
            
        self.nodes = []
        dfs(root)
        return self.nodes
# @lc code=end

