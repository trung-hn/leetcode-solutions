#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
# TAGS: Heap, BFS, DFS, Graph
# REVIEWME: Heap, Graph
class Solution:
    # 448 ms, 84.78%. Time: O(ElogE). Space: O(N + E). E is len(times). Dijkstra Algorithm
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w
        
        visited = {}
        heap = [(0, K)]
        while heap:
            cur_time, node = heapq.heappop(heap)
            if node in visited: continue
            visited[node] = cur_time
            for nei, time in graph[node].items():
                if nei in visited: continue
                heapq.heappush(heap, (time + cur_time, nei))
        return max(visited.values()) if len(visited) == N else -1
    
    # 448 ms, 84.78%. Time: O(NlogN). Space: O(N). Same as above but using set instead
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in times:
            graph[u][v] = w
        
        visited = set()
        heap = [(0, K)]
        while heap:
            cur_time, node = heapq.heappop(heap)
            visited.add(node)
            if len(visited) == N:
                return cur_time 
            for nei, time in graph[node].items():
                if nei in visited: continue
                heapq.heappush(heap, (time + cur_time, nei))
        return -1
# @lc code=end

