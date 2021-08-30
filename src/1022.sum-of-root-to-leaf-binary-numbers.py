#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#

# @lc code=start
# TAGS: Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    # 32 ms, 98%. Recursive DFS. Time O(N). Space O(H)
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, total=0):
            # Empty Node
            if not node:
                return 0

            # Increase total
            total = total * 2 + node.val

            # Leaf Nodes
            if node.left is node.right is None:
                return total

            # Recursion
            return dfs(node.left, total) + dfs(node.right, total)
        return dfs(root)

    # 32 ms, 98%. Iterative DFS Time O(N). Space O(N)
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = 0
        stack = [(root, 0)]
        while stack:
            node, total = stack.pop()

            # Empty Node
            if not node:
                continue

            # Increase total
            total = total * 2 + node.val

            # Leaf Nodes
            if node.left is node.right is None:
                ans += total
                continue

            # Stack
            stack.append((node.right, total))
            stack.append((node.left, total))
        return ans

    # 36 ms, 96%. BFS. Time: O(N). Space: O(N)
    def sumRootToLeaf(self, root: TreeNode) -> int:
        ans = []
        q = [(root, "")]
        for node, sofar in q:
            if node:
                sofar += str(node.val)
                if node.left is node.right is None:
                    ans.append(sofar)
                q.extend([(node.left, sofar), (node.right, sofar)])
        return sum(map(lambda x: int(x, 2), ans))
# @lc code=end
