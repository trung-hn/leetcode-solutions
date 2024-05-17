#
# @lc app=leetcode id=857 lang=python3
#
# [857] Minimum Cost to Hire K Workers
#


# @lc code=start
# TAGS: Array, Greedy, Sorting, Heap (Priority Queue)
class Solution:
    # Time: O(NlogN). Space: O(K)
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], k: int
    ) -> float:
        ratios = sorted((w / q, q) for q, w in zip(quality, wage))
        heap = []
        total_quality = 0
        ans = float("inf")
        for ratio, q in ratios:
            total_quality += q
            heapq.heappush(heap, -q)
            if len(heap) > k:
                total_quality += heapq.heappop(heap)
            if len(heap) == k:
                ans = min(ans, total_quality * ratio)
        return ans


# @lc code=end
