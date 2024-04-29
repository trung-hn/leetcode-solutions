#
# @lc app=leetcode id=2096 lang=python3
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#


# @lc code=start
# TAGS: String, Tree, Depth-First Search, Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:

        def make_graph(node=root, parent=None):
            if parent:
                neis[node.val].append((parent.val, "U"))
            if node.left:
                neis[node.val].append((node.left.val, "L"))
                make_graph(node.left, node)
            if node.right:
                neis[node.val].append((node.right.val, "R"))
                make_graph(node.right, node)

        def find_path(node=startValue, parent=None, sofar=[]):
            if node == destValue:
                self.ans = "".join(sofar)
                return
            for nei, di in neis[node]:
                if nei == parent:
                    continue
                sofar.append(di)
                find_path(nei, node, sofar)
                sofar.pop()

        self.ans = None
        neis = collections.defaultdict(list)
        make_graph()
        find_path()
        return self.ans


# @lc code=end
