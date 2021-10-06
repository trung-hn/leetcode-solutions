#
# @lc app=leetcode id=1962 lang=python3
#
# [1962] Remove Stones to Minimize the Total
#

# @lc code=start
# TAGS: Array, Heap


class Solution:
    # 1748 ms, 80.97%. Time: O(KlogN). Space: O(N)
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)
        for _ in range(k):
            biggest_pile = heapq.heappop(heap)
            # floor division of a negative number
            heapq.heappush(heap, biggest_pile // 2)
        return - sum(heap)


# @lc code=end
