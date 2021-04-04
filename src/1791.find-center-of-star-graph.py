#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#

# @lc code=start


class Solution:
    # 860 ms, 50%. Time and Space: O(N)
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = collections.Counter()
        for s, e in edges:
            counter[s] += 1
            counter[e] += 1
        return max(counter, key=counter.get)

    # 836 ms, 58.15%. Time and Space: O(1)
    def findCenter(self, edges: List[List[int]]) -> int:
        intersect = set(edges[0]) & set(edges[1])
        return intersect.pop()
# @lc code=end
