#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#

# @lc code=start
# TAGS: Dynamic Programming, Tree, DFS, Graph


class Solution:
    # 1032 ms, 48.48%. Time: O(V+E)
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        neis = collections.defaultdict(list)
        for s, e in edges:
            neis[s].append(e)
            neis[e].append(s)

        def dfs(node=0, parent=None):
            total = count = 0
            for nei in neis[node]:
                if nei != parent:
                    tot, cnt = dfs(nei, node)
                    total += tot
                    count += cnt
            trackers[node] = (total + count, count + 1)
            return trackers[node]

        def cal(node=0, frm_parent=0, parent=None):
            total = frm_parent + (n - trackers[node][1])
            ans[node] = total
            for nei in neis[node]:
                if nei != parent:
                    cal(nei, total - trackers[nei][1], node)

        trackers = {}
        ans = [0] * n
        dfs(0)
        cal(0, trackers[0][0])
        return ans
# @lc code=end
