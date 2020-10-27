#
# @lc app=leetcode id=1615 lang=python3
#
# [1615] Maximal Network Rank
#

# @lc code=start
# TAGS: Graph
class Solution:
    # 388 ms, 51.48%. Time: O(N^2). Space: O(N)
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads: return 0
        
        graph = collections.defaultdict(list)
        counter = [0] * n
        for frm, to in roads:
            counter[frm] += 1
            counter[to] += 1
            graph[frm].append(to)
            graph[to].append(frm)
        
        max_network_rank = 0
        for cnt1 in range(n):
            for cnt2 in range(cnt1 + 1, n):
                network_rank = self.get_network_rank(cnt1, cnt2, graph, counter)
                max_network_rank = max(max_network_rank, network_rank)
        return max_network_rank
        
    def get_network_rank(self, cnt1, cnt2, graph, counter):
        overlap = cnt1 in graph[cnt2]
        return counter[cnt1] + counter[cnt2] - overlap
    
    # 300 ms, 97.54%. Time: O(N^2). Space: O(N). Same complexity but slightly more optimized. 
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if not roads: return 0
        
        graph = collections.defaultdict(list)
        counter = [0] * n
        for frm, to in roads:
            counter[frm] += 1
            counter[to] += 1
            graph[frm].append(to)
            graph[to].append(frm)
        
        max_counter = max(counter)
        second_max_counter = 0
        for cnt in counter:
            if cnt != max_counter:
                second_max_counter = max(second_max_counter, cnt)
        
        new_counter = [i for i, cnt in enumerate(counter) if cnt in (max_counter, second_max_counter)]
        max_network_rank = 0
        for i, cnt1 in enumerate(new_counter):
            for cnt2 in new_counter[i + 1:]:
                overlap = cnt1 in graph[cnt2]
                max_network_rank = max(max_network_rank, counter[cnt1] + counter[cnt2] - overlap)
        return max_network_rank
    
# @lc code=end

