#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
# TAGS: Heap, Array, Binary Search
class Solution:
    # 108 ms, 100%. Time: O(MlogMlogN). Space: O(M)
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binary_search(row):
            lo, hi = 0, len(row)
            while lo < hi:
                mid = (lo + hi)//2
                if row[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        temp = sorted([(binary_search(row), i) for i, row in enumerate(mat)])
        return [i for v, i in temp][:k]
    
    # Time: O(MlogNlogK). Space: O(K)
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def binary_search(row):
            lo, hi = 0, len(row)
            while lo < hi:
                mid = (lo + hi)//2
                if row[mid]:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        heap = []
        for i, row in enumerate(mat):
            strength = binary_search(row)
            if len(heap) < k:
                heapq.heappush(heap, (-strength, -i))
            else:
                heapq.heappushpop(heap, (-strength, -i))
        rv = []
        while heap:
            strength, i = heapq.heappop(heap)
            rv.append(-i)
        return reversed(rv)
# @lc code=end

