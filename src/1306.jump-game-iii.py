#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start
# TAGS: BFS, DFS, Recursion
class Solution:
    # 208 ms, 91.23%. Time and Space: O(N)
    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]
        visited = set()
        while stack:
            i = stack.pop()
            if i < 0 or i >= len(arr) or i in visited: continue
            visited.add(i)
            if arr[i] == 0: return True
            stack.extend([i - arr[i], i + arr[i]])
        return False
        
            
# @lc code=end

