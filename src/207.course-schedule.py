#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
# TAGS: Breath First Search, Depth First Search, Graph, Topological Sort
# REVIEWME:
class Solution:
    # 104 ms, 64.59%. First attempt. Not a clean solution
    # Time and Space: O(N + E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        
        visited = [0]*numCourses
        self.ans = True
        def dfs(n):
            if visited[n] == 1:
                return
            if visited[n] == -1:
                self.ans = False
                return
            visited[n] = -1
            for i in graph[n]:
                dfs(i)
            visited[n] = 1
            
        for i in range(numCourses):
            dfs(i)
        return self.ans

    # 100 ms, 80.36%. Same complexity. Cleaner solution
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visited = [0]*numCourses
        def dfs(n):
            if visited[n] == 1: 
                return True
            if visited[n] == -1: 
                return False
            visited[n] = -1
            for i in graph[n]:
                if not dfs(i): 
                    return False
            visited[n] = 1
            return True
            
        return all(dfs(i) for i in range(numCourses))
              
# @lc code=end

