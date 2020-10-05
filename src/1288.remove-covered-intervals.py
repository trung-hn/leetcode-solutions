#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#

# @lc code=start
# TAGS: Greedy, Sort, Line Sweep
# REVIEWME: Greedy
class Solution:
    # 108 ms, 41.65%. Brute Force: Time: O(N^2). Space: O(N)
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda val: (val[0], -val[1]))
        covered = [0] * len(intervals)
        for i, (start1, end1) in enumerate(intervals):
            if covered[i]: continue
            for j in range(i + 1, len(intervals)):
                start2, end2 = intervals[j]
                if start2 >= end1: break
                if start1 <= start2 and end2 <= end1:
                    covered[j] = 1
        return len(covered) - sum(covered)

    # 88 ms, 98.31%. Greedy. Time: O(NlogN). Space: O(1), O(N) if consider sorting memory
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda val: (val[0], -val[1]))
        prev_end = -1
        cnt = 0
        for start, end in intervals:
            if end > prev_end:
                cnt += 1
                prev_end = end
        return cnt
# @lc code=end

