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
import heapq


class Solution:
    # 76 ms, 79.32%. O(NlogN). Space: O(N) because of sorting.
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        heap = []
        rooms = 0
        for start, end in sorted(intervals):
            while heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
            rooms = max(rooms, len(heap))
        return rooms
