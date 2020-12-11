#
# @lc app=leetcode id=1387 lang=python3
#
# [1387] Sort Integers by The Power Value
#

# @lc code=start
# TAGS: Sort, Graph
class Solution:
    # 152 ms, 93.85%. Time: O(NlogN). Space: O(N)
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = {1:0, 2:1}
        def get_pow(n):
            if n in power: return power[n]
            power[n] = 1 + (get_pow(3 * n + 1) if n % 2 else get_pow(n // 2))
            return power[n]
        return sorted(range(lo, hi + 1), key=get_pow)[k - 1]
    
    # 176 ms, 86.7. Time: O(NlogK). Space: O(N)
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power = {1:0, 2:1}
        def get_pow(n):
            if n in power: return power[n]
            power[n] = 1 + (get_pow(3 * n + 1) if n % 2 else get_pow(n // 2))
            return power[n]

        heap = []
        for ky in range(lo, hi + 1):
            val = get_pow(ky)
            if len(heap) < k:
                heapq.heappush(heap, (-val, -ky))
            else:
                heapq.heappushpop(heap, (-val, -ky))
        return -heap[0][1]
# @lc code=end

