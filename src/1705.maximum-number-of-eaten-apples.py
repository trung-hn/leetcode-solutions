#
# @lc app=leetcode id=1705 lang=python3
#
# [1705] Maximum Number of Eaten Apples
#

# @lc code=start
# TAGS: Heap, Greedy
class Solution:
    # 868 ms, 31.07%. Time: O(NlogN). Space: O(N)
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        day = eaten = 0
        while heap or day < len(apples):
            if day < len(apples):
                heapq.heappush(heap, (day + days[day], apples[day]))

            while heap and heap[0][0] <= day: heapq.heappop(heap)
                
            if heap:
                expired_day, amt = heapq.heappop(heap)
                if amt > 1:
                    heapq.heappush(heap, (expired_day, amt - 1))
                eaten += 1
            day += 1
        return eaten
    
    # 724 ms, 54.19%. Time: O(NlogN). Space: O(N). Slightly more optimized but longer
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        today = eaten = 0
        for amt, day in zip(apples, days):
            heapq.heappush(heap, (today + day, amt))
            while heap and heap[0][0] <= today: heapq.heappop(heap)
            
            if heap:
                expired_day, apples = heapq.heappop(heap)
                if apples > 1:
                    heapq.heappush(heap, (expired_day, apples - 1))
                eaten += 1
            today += 1
        
        while heap:
            while heap and heap[0][0] <= today:
                heapq.heappop(heap)
            if heap:
                expired_day, apples = heapq.heappop(heap)
                eaten += min(expired_day - today, apples)
            today += min(expired_day - today, apples)
        return eaten
# @lc code=end

