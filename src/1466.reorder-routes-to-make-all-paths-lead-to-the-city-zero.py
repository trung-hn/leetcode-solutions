#
# @lc app=leetcode id=1466 lang=python3
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
# TAGS: Tree, Depth First Search
class Solution:
    # 1012 ms, 74.19%. Time: O(|V|). Space: (|V|)
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        connections = set(tuple(val) for val in connections)
        graphs = collections.defaultdict(list)
        for a, b in connections:
            graphs[a].append(b)
            graphs[b].append(a)

        ans = 0
        visited = set()
        queue = [0]
        for node in queue:
            if node in visited: continue
            visited.add(node)
            
            for nxt in graphs[node]:
                if nxt in visited: continue
                if (nxt, node) not in connections:
                    ans += 1
            
            queue.extend(graphs[node])
        return ans

    # Clean solution from discussion.
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        reach = [True] + [False] * (n - 1)
        count = 0
        for i, j in connections:
            if reach[j]:
                reach[i] = True
            elif not reach[j]:
                reach[j] = True
                count += 1
        return count

# @lc code=end

