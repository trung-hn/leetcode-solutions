# TAGS: Tree, Premium
# REVIEWME: String, Stack
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    """
    76 ms, 57.42%. Time: O(N). Space: O(H)
    """
    def serialize(self, root: 'Node') -> str:
        def dfs(node):
            if not node: return ''
            rv = f"{node.val}["
            for child in node.children:
                rv += dfs(child) + " "
            return rv[:-1] if rv[-1] == '[' else rv + ']'
        # print(dfs(root))
        return dfs(root)
	
    def deserialize(self, data: str) -> 'Node':
        if not data: return None
        
        root = node = Node(None, [])
        data += ' '; num = 0; stack = []
        for i in range(len(data)):
            c = data[i]
            if i > 0: c_prev = data[i - 1]
            if c == "[":
                stack.append(node)
                node = Node(num, [])
                num = 0
                
            elif c == "]":
                parent = stack.pop()
                parent.children.append(node)
                node = parent
                num = 0
            
            elif c.isdigit():
                num = num * 10 + int(c)
            
            elif c == " " and c_prev != "]":
                node.children.append(Node(num,[]))
                num = 0
                
        return root.children[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))