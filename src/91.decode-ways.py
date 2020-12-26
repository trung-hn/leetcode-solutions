#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
# TAGS: String, Dynamic Programming
class Solution:
    # 28 ms, 86.26%. topdown with memoization. Time and Space: O(N).  
    def numDecodings(self, s: str) -> int:
        visited = {}
        def dfs(i = 0):
            if i in visited: return visited[i]
            if i >= len(s): return 1
            if s[i] == '0': return 0
            rv = dfs(i + 1)
            if i + 1 < len(s) and int("".join(s[i : i + 2])) <= 26:
                rv += dfs(i + 2)
            visited[i] = rv
            return rv
        return dfs()
        
# @lc code=end

