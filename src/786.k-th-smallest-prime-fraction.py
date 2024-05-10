#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#


# @lc code=start
# TAGS: Array, Two Pointers, Binary Search, Sorting, Heap (Priority Queue)
# REVIEWME: Heap
import heapq


class Solution:
    # Time: O(KlogK). Space: O(K)
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        N = len(arr)
        heap = [
            (arr[i] / arr[-1], i, N - 1) for i in range(N)
        ]  # micro optimization: range(min(k, N))
        heapq.heapify(heap)
        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            ratio = arr[i] / arr[j - 1]
            heapq.heappush(heap, (ratio, i, j - 1))
        _, i, j = heap[0]
        return arr[i], arr[j]


# @lc code=end
