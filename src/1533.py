# TAGS: Premium, Binary Search
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    # 260 ms, 72.62%. Time: O(logN). Space: O(1)
    def getIndex(self, reader: 'ArrayReader') -> int:
        lo, hi = 0, reader.length() - 1
        while lo < hi:
            mid = (lo + hi) / 2
            m1 = math.floor(mid)            
            m2 = math.ceil(mid)
            result = reader.compareSub(lo, m1, m2, hi)
            if result == 0:
                return m1
            elif result == 1:
                hi = m1
            else:
                lo = m2
        return lo