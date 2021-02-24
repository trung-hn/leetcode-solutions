#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#

# @lc code=start
# TAGS: Array, Dynamic Programming
class Solution:
    # 556 ms, 89.27%. Time: O(N^2). Space: O(N^2)
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        indices = {val:i for i, val in enumerate(arr)}
        
        pairs = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                nxt = indices.get(arr[i] + arr[j], -1)
                if nxt > j: pairs.append((j, nxt))
                    
        if not pairs: return 0
        
        length = 2
        while pairs:
            cur = []
            length += 1
            for i, j in pairs:
                nxt = indices.get(arr[i] + arr[j], -1)
                if nxt > j: cur.append((j, nxt))
            pairs = cur
        return length
                    
# @lc code=end

