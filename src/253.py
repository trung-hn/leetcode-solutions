"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
"""

# TAGS: Premium, Heap, Greedy, Sort
# REVIEWME: Heap

class Solution:
    # Not working.
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        intervals.sort()
        
        heap = []
        
        longest_overlap = overlap = end_soonest = 0
        for start, end in intervals:
            # print(heap)
            if start >= end_soonest:
                while heap and start >= end_soonest:
                    end_soonest = heapq.heappop(heap)
                    overlap -= 1
                if not heap:
                    end_soonest = end
                    overlap = 0
            elif start < end_soonest:
                if end_soonest < end:
                    heapq.heappush(heap, end)
                else:
                    heapq.heappush(heap, end_soonest)
                    end_soonest = end
                overlap += 1
            longest_overlap = max(longest_overlap, overlap)
        return longest_overlap + 1
    
    # Need hint. When we need a room, check if previous room is freed using heap
    # 76 ms, 79.32%. O(NlogN). Space: O(N) because of sorting.
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort()
        heap = []
        
        rooms = 0
        for start, end in intervals:
            while heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            rooms = max(rooms, len(heap))
        return rooms
        
        
        
        
        