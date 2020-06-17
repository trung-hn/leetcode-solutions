#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start
# TAGS: Dynamic Programming, Heap, Breadth First Search:
# REVIEWME:  Dijkstra's Algorithm, Graph, 
class Solution:
    """
    Read article for more info about complexity and other solutions
    """
    # 104 ms, 69.88%.
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graphs = collections.defaultdict(list)
        for s, d, w in flights:
            graphs[s].append([d, w])
        
        dist_tbl = [float("inf")]*n
        stops_tbl = [float("inf")]*n
        min_heap = [[0, 0, src]]
        while min_heap:
            weight, k, dest = heapq.heappop(min_heap)
            
            if dest == dst:
                break

            if k == K + 1:
                continue
            
            for nxt_dst, next_w in graphs[dest]:
                if next_w + weight < dist_tbl[nxt_dst]:
                    dist_tbl[nxt_dst] = next_w + weight
                    heapq.heappush(min_heap, [next_w + weight, k + 1, nxt_dst])

                elif k < stops_tbl[nxt_dst]:
                    # Also consider case with longer distance but less stops. 
                    stops_tbl[nxt_dst] = next_w + weight
                    heapq.heappush(min_heap, [next_w + weight, k + 1, nxt_dst])

        return dist_tbl[dst] if dist_tbl[dst] != float("inf") else -1
            
# @lc code=end

