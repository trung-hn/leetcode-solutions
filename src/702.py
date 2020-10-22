# TAGS: Premium, Binary Search
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    # Time: O(logN). Space: O(1)
    def search(self, reader, target):
        
        lo, hi = 0, 10000
        while lo < hi:
            mid = (lo + hi) // 2
            if reader.get(mid) >= target:
                hi = mid
            else:
                lo = mid + 1
        if reader.get(lo) == target:
            return lo
        return -1