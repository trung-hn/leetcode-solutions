#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
# TAGS: Design, hard, heap, 
# REVIEWME:
# 224 ms, 43.41%. Time: O(n), Space: O(n)
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num = []
    # O(N)
    def addNum(self, num: int) -> None:
        bisect.insort(self.num, num)
    # O(1)
    def findMedian(self) -> float:
        mid = (len(self.num) - 1) // 2
        if len(self.num) % 2:
            return self.num[mid]
        else:
            return sum(self.num[mid:mid + 2]) /2

# 196 ms, 85.59%. Time: O(log n), Space: O(n)
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        heapq.heapify(self.max_heap)
        self.min_heap = []
        heapq.heapify(self.min_heap)
        self.cnt = 0
    # O(log n)
    def addNum(self, num: int) -> None:
        self.cnt += 1
        
        # Always add to max_heap first
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Self Balancing heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)
        
    # O(1)
    def findMedian(self) -> float:
        v1 = -self.max_heap[0]
        
        # Edge case: min_heap is empty
        v2 = self.min_heap[0] if not self.cnt % 2 else v1
        return (v1 + v2) / 2
      
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

