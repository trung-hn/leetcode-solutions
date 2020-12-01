#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
# REVIEW: Divide and Conquer, Heap, Binary Indexed Tree, Segment Tree, Line Sweep
class Solution:
    """ 
    Explanation: 
    https://leetcode.com/problems/the-skyline-problem/discuss/61197/(Guaranteed)-Really-Detailed-and-Good-(Perfect)-Explanation-of-The-Skyline-Problem
    """
    # Does not work because of edge cases, but the idea is correct
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        critical_points = []
        for key, (left, right, _) in enumerate(buildings):
            critical_points.append((left, key))
            critical_points.append((right, key))
        
        critical_points.sort()
        ans = []; heap = []
        visited = set()
        for critical_point, key in critical_points:
            if key in visited: # end of a rectangle
                visited.discard(key) 
                while heap and heap[0][1] <= critical_point:
                    # as long as right edge <= curr, we pop
                    # another way to deal with passed building is to use external pointers.
                    heapq.heappop(heap)
            else: # start of a rectangle
                visited.add(key) 
                l, r, h = buildings[key]
                heapq.heappush(heap, (-h, r)) # push height and right edge to heap
            
            if heap:
                if not ans or ans[-1][-1] != -heap[0][0]: # only add when there is difference in height
                    ans.append([critical_point, -heap[0][0]])
            else:
                ans.append([critical_point, 0])
        return ans

    # Similar to: https://leetcode.com/problems/the-skyline-problem/discuss/61261/10-line-Python-solution-104-ms
    # 108 ms, 86.42%. Time: O(NlogN). Space: O(N)
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        critical_points = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        heap = [(0, float("inf"))]; ans = []
        for L, negH, R in critical_points:
            while L >= heap[0][1]:
                heapq.heappop(heap)
            if negH:
                heapq.heappush(heap, (negH, R))
            if not ans or -heap[0][0] != ans[-1][-1]:
                ans.append([L, -heap[0][0]])
        return ans
# @lc code=end

