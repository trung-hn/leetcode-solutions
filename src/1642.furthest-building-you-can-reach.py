#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#

# @lc code=start
# TAGS: Binary Search, Heap
import heapq


class Solution:
    # 412 ms, 86.22%. Time: O(NlogN). Space: O(N)
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        ans = 0
        for b1, b2 in zip(heights, heights[1:]):
            if b1 < b2:
                heapq.heappush(heap, b2 - b1)
                if len(heap) > ladders:
                    bricks -= heapq.heappop(heap)
                if bricks < 0:
                    break
            ans += 1
        return ans


# @lc code=end
