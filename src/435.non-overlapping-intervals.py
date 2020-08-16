#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
# TAGS: Greedy
# REVIEWME: Tricky, Discussion. 
class Solution:
    # 76 ms, 71%. Time: O(NlogN) because of sorting. Space: O(1)
    # Approach and explanation: https://leetcode.com/problems/non-overlapping-intervals/discuss/793070/Python-O(n-log-n)-sort-ends-with-proof-explained
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        n, count = len(intervals), 1
        if n == 0: return 0
        curr = intervals[0]
        
        for interval in intervals:
            if curr[1] <= interval[0]:
                count += 1
                curr = interval
                
        return n - count  
# @lc code=end

