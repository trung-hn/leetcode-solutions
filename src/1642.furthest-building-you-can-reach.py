#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#

# @lc code=start
# TAGS: Binary Search, Heap
class Solution:
    # 580 ms, 45.4%. Time: O(NlogN). Space: O(N)
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        cnt = 0
        for b1, b2 in zip(heights, heights[1:]):
            if b1 < b2:
                heapq.heappush(heap, b2 - b1)
                delta_h = 0
                if len(heap) > ladders:
                    delta_h = heapq.heappop(heap)
                bricks -= delta_h
                if bricks < 0: break
            cnt += 1
        return cnt
# @lc code=end

