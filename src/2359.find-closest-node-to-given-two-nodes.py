#
# @lc app=leetcode id=2359 lang=python3
#
# [2359] Find Closest Node to Given Two Nodes
#

# @lc code=start
# TAGS: DFS, Graph
from typing import List


class Solution:
    # Time and Space: O(N)
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_dist_arr(init_node):
            depth = [-1] * len(edges)
            depth[init_node] = 0
            node = init_node
            while edges[node] != -1:  # nxt exists
                nxt = edges[node]
                if depth[nxt] > -1:  # visited
                    break
                depth[nxt] = depth[node] + 1
                node = nxt
            return depth

        depth1 = get_dist_arr(node1)
        depth2 = get_dist_arr(node2)
        min_val = float("inf")
        min_arg = -1
        for i, (v1, v2) in enumerate(zip(depth1, depth2)):
            if -1 in (v1, v2):
                continue
            if max(v1, v2) < min_val:
                min_val = max(v1, v2)
                min_arg = i
        return min_arg


# @lc code=end
