#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#

# @lc code=start
# TAGS: Tree, Depth First Search
# REVIEWME: Tricky problem. 
class Solution:
    # TLE. BFS. Slow because of `in sofar`
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        no_apples = hasApple.count(True)
        graph = collections.defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        queue = [(0, 0, 0, [])]
        for node, step, cnt, sofar in queue:
            if cnt == no_apples and node == 0:
                return step
            if hasApple[node] and node not in sofar:
                cnt += 1
            for nxt in graph[node]:
                queue.append((nxt, step + 1, cnt, sofar + [node]))
        return 0

    # 702 ms, 80.02%. DFS, Time: O(E), Space: O(E)
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = collections.defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        visited = set()
        def dfs(node):
            if node in visited: return 0
            visited.add(node)
            total = 0
            for child in graph[node]:
                total += dfs(child)
            if node != 0 and (hasApple[node] or total):
                total += 2
            return total
        return dfs(0)        
# @lc code=end

