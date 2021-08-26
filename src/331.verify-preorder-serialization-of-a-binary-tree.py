#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
# TAGS: String, Stack, Tree, Binary Tree


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return f"{self.val}:({str(self.left)}, {str(self.right)})"


class Solution:
    # Time and Space: O(N). Simulation
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == "#":
            return True

        def dfs(node=None):
            if self.ptr >= len(nodes):
                return None

            # End node
            if nodes[self.ptr] == "#":
                self.ptr += 1
                return None
            # Assign value to par
            node = TreeNode(nodes[self.ptr])
            # increase ptr
            self.ptr += 1

            # dfs to children
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            return node

        nodes = preorder.split(",")
        self.ptr = 0
        dfs()
        return self.ptr == len(nodes) and nodes[-2:] == ["#", "#"]

    # 47 ms, 11.27%. Time and Space: O(N). Short Simulation
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == "#":
            return True

        def dfs():
            if self.ptr >= len(nodes):
                return
            self.ptr += 1
            # Assign value to par
            if nodes[self.ptr - 1] != "#":
                dfs()
                dfs()
            return

        nodes = preorder.split(",")
        self.ptr = 0
        dfs()
        return self.ptr == len(nodes) and nodes[-2:] == ["#", "#"]

    # Stack solution. Time and Space: O(N)
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for node in preorder.split(","):
            stack.append(node)
            while len(stack) > 2 and stack[-1] == stack[-2] == "#" and stack[-3] != "#":
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        return stack == ["#"]

# @lc code=end
