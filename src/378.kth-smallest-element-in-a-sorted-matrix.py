#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
# TAGS: Heap, Binary Search
import heapq
class Solution:
    """
    There are better solutions in article and discussion
    """
    # Time: O(N^2logK). Space: O(K)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return 0
        heap = []
        for row in matrix:
            for val in row:
                if len(heap) < k:
                    heapq.heappush(heap, -val)
                elif -val > heap[0]:
                    heapq.heappushpop(heap, -val)
        return -heap[0]
# @lc code=end

