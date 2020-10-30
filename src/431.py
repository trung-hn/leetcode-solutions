# TAGS: Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    "Scheme: first child on the left node, siblings on the right node"
    # 76 ms, 68.71%. Time: O(N). Space: O(H)
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root: return None
        def make_binarytree(nodes):
            if not nodes: return None
            rv = TreeNode(nodes[0].val)
            rv.right = make_binarytree(nodes[1:])
            rv.left = make_binarytree(nodes[0].children)
            return rv
        return make_binarytree([root])
        
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data: return None
        def make_narytree(node):
            if not node: return
            rv = Node(node.val, [])
            child = node.left
            while child:
                rv.children.append(make_narytree(child))
                child = child.right
            return rv
        return make_narytree(data)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))