#
# @lc app=leetcode id=919 lang=python3
#
# [919] Complete Binary Tree Inserter
#

# @lc code=start
# TAGS: Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:
    # 100 ms, 13.59%. 
    # Time: O(N). Space: O(1)
    def __init__(self, root: TreeNode):
        self.root = root
        def count(node):
            if not node: return 0
            return count(node.left) + count(node.right) + 1
        self.cnt = count(root)

    # Time: O(logN). Space: O(1)
    def insert(self, v: int) -> int:
        self.cnt += 1
        bi = bin(self.cnt)[3:]
        node = self.root
        for c in bi[:-1]:
            node = node.left if c == '0' else node.right
        
        if node.left:
            node.right = TreeNode(v)
        else:
            node.left = TreeNode(v)
            
        return node.val
    
    # Time: O(1). Space: O(1)
    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
# @lc code=end

