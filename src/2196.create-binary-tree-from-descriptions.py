#
# @lc app=leetcode id=2196 lang=python3
#
# [2196] Create Binary Tree From Descriptions
#

# @lc code=start
# TAGS: DFS, BFS, Binary Tree, Tree, Hash Table, Array
# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Time adn Space: O(n)
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        parents = set()
        children = set()
        graph = collections.defaultdict(list)
        for parent, child, left in descriptions:
            graph[parent].append((child, left))
            parents.add(parent)
            children.add(child)

        grand = (parents - children).pop()
        root = curr = TreeNode(grand)
        queue = [curr]
        for node in queue:
            for child, is_left in graph[node.val]:
                if is_left:
                    node.left = TreeNode(child)
                    queue.append(node.left)
                else:
                    node.right = TreeNode(child)
                    queue.append(node.right)
        return root


# @lc code=end
