#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#

# @lc code=start
# TAGS: Array, Greedy, Heap, Ordered Set
from typing import List
import heapq


class Solution:
    # 1419 ms, 52.43%. Time: O(NlogN). Space: O(N)
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = [-num * 2 if num % 2 else -num for num in nums]
        heapq.heapify(heap)
        ans = float("inf")
        xmin = -max(heap)
        while True:
            xmax = -heapq.heappop(heap)
            ans = min(ans, xmax - xmin)
            if xmax % 2:
                return ans
            half = xmax // 2
            heapq.heappush(heap, -half)
            xmin = min(xmin, half)
# @lc code=end
