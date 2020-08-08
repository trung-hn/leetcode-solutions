#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# TAGS: Tree
# REVIEWME: Tricky, Hard
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 356 ms, 53.68%.
    def pathSum(self, root: TreeNode, target: int) -> int:
        q = collections.deque([[root, []]])
        cnt = 0
        while q:
            node, sofar = q.popleft()
            if node:
                if node.val == target: cnt += 1
                temp = [node.val]
                for val in sofar:
                    new_val = val + node.val
                    if new_val == target: cnt += 1
                    temp.append(new_val)
                #print(cnt, node.val, sofar, temp)
                q.append([node.left, tuple(temp)])
                q.append([node.right, tuple(temp)])
                
        return cnt
    
    # Not correct because nodes are repeated multiple times.
    def pathSum1(self, root: TreeNode, target: int) -> int:
        print("----")
        self.ans = 0
        def dfs(node, sofar=0, alls=[]):
            if not node: return
            if sofar + node.val == target:
                print(node.val, alls)
                self.ans += 1
            dfs(node.left, sofar + node.val, alls + [node.val])
            dfs(node.right, sofar + node.val, alls + [node.val])
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans

    # From solution article. Time and Space: O(N)
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node:
                return 
            
            # current prefix sum
            curr_sum += node.val
            
            # here is the sum we're looking for
            if curr_sum == k:
                count += 1
            
            # number of times the curr_sum − k has occurred already, 
            # determines the number of times a path with sum k 
            # has occurred up to the current node
            count += h[curr_sum - k]
            
            # add the current sum into hashmap
            # to use it during the child nodes processing
            h[curr_sum] += 1
            
            # process left subtree
            preorder(node.left, curr_sum)
            # process right subtree
            preorder(node.right, curr_sum)
            
            # remove the current sum from the hashmap
            # in order not to use it during 
            # the parallel subtree processing
            h[curr_sum] -= 1
            
        count, k = 0, sum
        h = defaultdict(int)
        preorder(root, 0)
        return count
# @lc code=end

