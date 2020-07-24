#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
# TAGS: Backtracking, Depth First Search
class Solution:
    # 92 ms, 99%. Time and Space: O(2^N * N)
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.ans = []
        def dfs(start=0, sofar=[]):
            if start == len(graph)-1:
                self.ans.append(sofar + [start])
                return
            for node in graph[start]:
                dfs(node, sofar + [start])
        dfs()
        return self.ans
            
# @lc code=end

