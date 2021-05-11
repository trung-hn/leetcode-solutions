#
# @lc app=leetcode id=1042 lang=python3
#
# [1042] Flower Planting With No Adjacent
#

# @lc code=start
# TAGS: Graph


class Solution:
    # 448 ms, 51.02%. Time and Space: O(|V|+|E|)
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # Edges
        neis = collections.defaultdict(list)
        for s, e in paths:
            neis[s].append(e)
            neis[e].append(s)

        flowers = [0] * (n + 1)

        def dfs(node, parent=-1):
            nei_flowers = set(flowers[nei] for nei in neis[node])

            # Try all flower options
            option = 1
            while option in nei_flowers:
                option += 1

            # Assign flower to position
            flowers[node] = option

            # DFS neighbor
            for nei in neis[node]:
                # Skip visited positions
                if flowers[nei]:
                    continue
                dfs(nei, node)

        # Try all disconnected groups
        for i in range(n + 1):
            if not flowers[i]:
                dfs(i)
        return flowers[1:]

# @lc code=end
