#
# @lc app=leetcode id=1753 lang=python3
#
# [1753] Maximum Score From Removing Stones
#

# @lc code=start
# TAGS: Math, Heap


class Solution:
    # 824 ms, 18.97%. Time: O(N). Space: O(1). Heap solution, Greedy
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapq.heapify(heap)
        score = 0
        while len(heap) > 1:
            n1, n2 = heapq.heappop(heap), heapq.heappop(heap)
            score += 1
            for n in (n1, n2):
                if n < -1:
                    heapq.heappush(heap, n + 1)
        return score

    # 20 ms, 99.86%. Time and Space: O(1). Math solution
    def maximumScore(self, a: int, b: int, c: int) -> int:
        a, b, c = sorted([a, b, c])
        if a + b <= c:
            return a + b
        # notice that this is floor division, it covers case when not all piles are depleted
        return (a + b + c) // 2
# @lc code=end
