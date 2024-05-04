#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
# TAGS: Hash Table, Design, Heap (Priority Queue)
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.ptr = 1
        self.heap = []
        self.seen = set()

    def popSmallest(self) -> int:
        if self.heap:
            self.seen.discard(self.heap[0])
            return heapq.heappop(self.heap)
        self.ptr += 1
        return self.ptr - 1

    def addBack(self, num: int) -> None:
        if num in self.seen or num >= self.ptr:
            return
        self.seen.add(num)
        heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end
