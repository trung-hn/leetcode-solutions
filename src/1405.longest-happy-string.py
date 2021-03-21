#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#

# @lc code=start
# TAGS: Greedy, Dynamic Programming


class Solution:
    # 24 ms, 94.96%. Time: O(N) Space: O(N) N = sum(a, b, c)
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for f, c in (-a, 'a'), (-b, 'b'), (-c, 'c'):
            if f:
                heap.append((f, c))
        heapq.heapify(heap)
        ans = []
        while heap:
            f, c = heapq.heappop(heap)
            if len(ans) >= 2 and ans[-1] == ans[-2] == c:
                if not heap:
                    break
                f2, c2 = heapq.heapreplace(heap, (f, c))
                ans.append(c2)
                if f2 < -1:
                    heapq.heappush(heap, (f2 + 1, c2))
            else:
                ans.append(c)
                if f < -1:
                    heapq.heappush(heap, (f + 1, c))
        return "".join(ans)


# @lc code=end
