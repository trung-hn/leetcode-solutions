#
# @lc app=leetcode id=1792 lang=python3
#
# [1792] Maximum Average Pass Ratio
#

# @lc code=start
# TAGS: Heap


class Solution:
    # 2588 ms, 89.07%. Time: O(N + KlogN). Space: O(N)
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(p/t - (p+1)/(t+1), p, t) for p, t in classes]
        heapq.heapify(heap)
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (p/t - (p+1)/(t+1), p, t))
        return sum(p/t for _, p, t in heap) / len(heap)
# @lc code=end
