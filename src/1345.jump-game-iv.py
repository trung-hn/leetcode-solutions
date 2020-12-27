#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#

# @lc code=start
# TAGS: BFS
# REVIEWME: BFS
import collections
class Solution:
    # 560 ms, 65.78%. Time and Space: O(N)
    def minJumps(self, arr: List[int]) -> int:
        pos = collections.defaultdict(list)
        for i, val in enumerate(arr):
            pos[val].append(i)
            
        visited = {}
        queue = [0]; depth = 0
        while queue:
            cur = []
            for index in queue:
                if index in visited and visited[index] <= depth: continue
                visited[index] = depth
                
                # Terminate condition
                if index == len(arr) - 1: return depth

                # BFS 2 ways
                cur.append(index + 1)
                if index: cur.append(index - 1)

                # BFS others index with same value
                for j in pos[arr[index]]:
                    cur.append(j)
                    
                del pos[arr[index]]
            depth += 1
            queue = cur
# @lc code=end

