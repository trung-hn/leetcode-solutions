# TAGS: Binary Search, Tree, Premium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 40 ms, 80%. Time and Space: O(H)
    def closestValue(self, root: TreeNode, target: float) -> int:
        self.ans = None
        self.diff = float("inf")
        def dfs(node, target):
            if not node: return
            if self.diff > abs(target - node.val):
                self.diff = abs(target - node.val)
                self.ans = node.val
            if node.val > target: 
                dfs(node.left, target)
            else:
                dfs(node.right, target)
        dfs(root, target)
        return self.ans
    
    # 36 ms, 94.51%. Time: O(H), Space: O(1)
    def closestValue(self, root: TreeNode, target: float) -> int:
        ans = None
        diff = float("inf")
        while root:
            if diff > abs(target - root.val):
                diff = abs(target - root.val)
                ans = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
    
        return ans