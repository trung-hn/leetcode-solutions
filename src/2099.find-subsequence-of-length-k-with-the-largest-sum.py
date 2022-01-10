#
# @lc app=leetcode id=2099 lang=python3
#
# [2099] Find Subsequence of Length K With the Largest Sum
#

# @lc code=start
# TAGS: Array, Hash Table, Sotring, Heap
from typing import List


class Solution:
    # 48 ms, 97.20%. Time: O(NlogN). Space: O(N)
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = [(val, i) for i, val in enumerate(nums)]
        arr.sort()
        arr = sorted(arr[-k:], key=lambda x: x[1])
        return [val for val, _ in arr]

    # 48 ms, 97.20%. Time: O(NlogK). Space: O(K). Using Heap

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i, val in enumerate(nums):
            heapq.heappush(heap, (val, i))
            if len(heap) > k:
                heapq.heappop(heap)
        heap.sort(key=lambda x: x[1])
        return [val for val, _ in heap]
# @lc code=end
