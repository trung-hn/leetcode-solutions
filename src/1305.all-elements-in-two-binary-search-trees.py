#
# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#

# @lc code=start
# TAGS: Sort, Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 588 ms, 22.97%. Time: O(N). Space: O(N)
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        
        ans = []
        L1, L2 = inorder(root1), inorder(root2)
        
        i = j = 0
        while i < len(L1) and j < len(L2):
            if L1[i] < L2[j]:
                ans.append(L1[i])
                i += 1
            else:
                ans.append(L2[j])
                j += 1
        ans.extend(L1[i:])
        ans.extend(L2[j:])
        return ans


    # 356 ms, 83.41 %. Time: O(N). Space: O(N). 
    # Although this use sort, it is still O(N) because of the nature or tim sort
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        nums = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root1)
        inorder(root2)

        return sorted(nums)

# @lc code=end

