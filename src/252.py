# TAGS: Premium, Sort
class Solution:
    # 76 ms, 91%
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda interval: interval[0])
        for (_, end0), (start1, _) in zip(intervals, intervals[1:]):
            if end0 > start1:
                return False
        return True
    
    # 76 ms, 91%
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(end <= start for (_, end), (start, _) in zip(intervals, intervals[1:]))