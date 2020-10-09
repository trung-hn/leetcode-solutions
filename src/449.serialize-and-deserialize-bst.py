#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
# TAGS: Tree
# REVIEWME: Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """ 80 ms. Time: O(NlogN) because of Binary Search. Space:O(N)"""
    def serialize(self, root: TreeNode) -> str:
        def pre_order(node):
            return [str(node.val)] + pre_order(node.left) + pre_order(node.right) if node else []
        return " ".join(pre_order(root))
        
    def deserialize(self, data: str) -> TreeNode:
        def binary_search(i, j, target):
            if target > values[j]: return j + 1
            lo, hi = i, j
            while lo < hi:
                mid = (lo + hi) // 2
                if values[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        def linear_search(i, j, target):
            for k in range(i, j + 1):
                if target < values[k]:
                    return k
            return j + 1
            
        values = [int(val) for val in data.split()]
        def dfs(i, j):
            if i > j: return None
            root = TreeNode(values[i])
            cut_off = binary_search(i + 1, j, root.val)
            root.left = dfs(i + 1, cut_off - 1)
            root.right = dfs(cut_off, j)
            return root
        return dfs(0, len(values) - 1)
    
    # Similar to above but we move the whole array instead. 
    def deserialize1(self, data: str) -> TreeNode:
        def linear_search(array, target):
            for i in range(len(array)):
                if array[i] > target:
                    return i
            return len(array)

        def dfs(array):
            if not array: return
            root = TreeNode(array[0])
            cut_off = linear_search(array[1:], root.val) + 1
            root.left = dfs(array[1:cut_off])
            root.right = dfs(array[cut_off:])
            return root
        
        values = [int(val) for val in data.split()]
        return dfs(values)

class Codec:
    """ 80 ms. From Article. Time and Space: O(N) because we use post_order"""
    def serialize(self, root):
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data):
        def dfs(lower = float('-inf'), upper = float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            
            val = data.pop()
            root = TreeNode(val)
            root.right = dfs(val, upper)
            root.left = dfs(lower, val)
            return root
        
        data = [int(x) for x in data.split(' ') if x]
        return dfs()        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end

