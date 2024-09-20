#
# @lc app=leetcode id=3092 lang=python3
#
# [3092] Most Frequent IDs
#

# @lc code=start
# TAGS: Array, Hash Table, Heap (Priority Queue), Ordered Set
from heapq import heappop, heappush
from collections import defaultdict
from sortedcontainers import SortedDict


class Solution:
    # Using dict and heap.
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        heap, ans = [], []
        counter = defaultdict(int)
        for n, f in zip(nums, freq):
            counter[n] += f
            heappush(heap, (-counter[n], n))
            while -heap[0][0] != counter[heap[0][1]]:
                heappop(heap)
            ans.append(-heap[0][0])
        return ans

    # Using sortedcontainers
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        def add(key, val):
            meta_counter[key] = meta_counter.get(key, 0) + val
            if meta_counter[key] <= 0:
                del meta_counter[key]

        meta_counter = SortedDict()
        counter = defaultdict(int)
        ans = []
        for n, f in zip(nums, freq):
            counter[n] += f
            add(counter[n], 1)
            add(counter[n] - f, -1)
            ans.append(meta_counter.peekitem(-1)[0])
        return ans


# @lc code=end
