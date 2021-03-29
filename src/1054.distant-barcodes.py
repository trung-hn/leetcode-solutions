#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#

# @lc code=start
# TAGS: Sort, Heap


class Solution:
    """
    There is a O(N) solution in the dicussion (Math)
    """
    # 488 ms, 53.11%. Time: O(NlogN). Space: O(N)

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        # Get counter
        counter = collections.Counter(barcodes)
        # Heapify frequency
        heap = [(-f, v) for v, f in counter.items()]
        heapq.heapify(heap)
        result = []
        # Heap sort
        while heap:
            f, v = heapq.heappop(heap)
            if result and result[-1] == v:
                temp = heapq.heapreplace(heap, (f, v))
                f, v = temp
            result.append(v)
            if f < -1:
                heapq.heappush(heap, (f + 1, v))
        return result


# @lc code=end
