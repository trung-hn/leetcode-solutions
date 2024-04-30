#
# @lc app=leetcode id=2049 lang=python3
#
# [2049] Count Nodes With the Highest Score
#

# @lc code=start
# TAGS: Array, Tree, Depth-First Search, Binary Tree
from collections import defaultdict, Counter


class Solution:
    # Time: O(N). Space :O(N)
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def populate_children(node):
            for nei in neis[node]:
                children[node] += populate_children(nei)
            return children[node]

        def get_max_score(node):
            product = (len(parents) - children[node]) or 1
            for nei in neis[node]:
                product *= children[nei]
            ans[product] += 1

            for nei in neis[node]:
                get_max_score(nei)

        neis = defaultdict(list)
        for n, p in enumerate(parents):
            neis[p].append(n)
        children = defaultdict(lambda: 1)
        populate_children(0)
        ans = Counter()
        get_max_score(0)
        return ans[max(ans)]


# @lc code=end
