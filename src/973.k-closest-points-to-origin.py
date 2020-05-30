#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
# TAGS: Divide and Conquer, Heap, Sort
# REVIEWME: typical Heap problem. There is a divide and conquer solution in the article
class Solution:
    # 660 ms, 94%. O(NlogN) because of sorting
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def custom_key(xy):
            x, y = xy
            return x**2 + y**2
        points.sort(key=custom_key)
        return points[:K]
    
    # 1160 ms, 7.5%. Priority Queue. O(N logK). Space O(K).
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def custom_key(xy):
            x, y = xy
            return x**2 + y**2
        import queue
        storage = queue.PriorityQueue()
        for point in points:
            storage.put((-custom_key(point), point))
            if storage.qsize() > K: storage.get()
        rv = [storage.get()[1] for _ in range(K)]
        return rv
    
    # 656 ms, 95.55%. Similar to above. Heapq. O(NlogK). Space O(K)
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        storage = []
        heapq.heapify(storage)
        for x, y in points:
            dist = -(x*x + y*y)
            if len(storage) < K:
                heapq.heappush(storage, (dist, (x,y)))
            else:
                heapq.heappushpop(storage, (dist, (x,y)))
        return [point for d, point in storage]
# @lc code=end

