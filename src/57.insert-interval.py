#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
# TAGS: Array, Sort, Greedy
# REVIEWME: Hard, Pythonic, Clever. 
class Solution:
    """
    3 Clean solutions from lee:
    https://leetcode.com/problems/insert-interval/discuss/21622/7%2B-lines-3-easy-solutions
    """
    # 96 ms, 35.34 %. Time and Space: O(N) although we use binary search just because we need to combine at the end anyway
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[0] > intervals[-1][-1]:
            return intervals + [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        
        def search(target):
            lo, hi = 0, len(intervals)
            while lo < hi:
                mid = (lo + hi) // 2
                if intervals[mid][0] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        start = search(newInterval[0])
        end = search(newInterval[1])
        
        # If not the first index and smaller than the previous end => move start back 1 index. This will:
        # 1. merge with the previous of that's the case
        # 2. create a new array if that's not the case
        if start and intervals[start - 1][1] >= newInterval[0]:
            start -= 1
        
        # Check if new interval ending is smaller than current start:
        # If that's the case, it will create a new array or merge with the previous
        # Else, it will merge with the current. 
        if end == len(intervals) or intervals[end][0] > newInterval[1]:
            end -= 1
        
        if start == -1:
            return [[newInterval[0], max(newInterval[1], intervals[end][1])]] + intervals[end + 1:]
            
        return intervals[:start] + [[min(newInterval[0], intervals[start][0]), max(newInterval[1], intervals[end][1])]] + intervals[end + 1:]
    
    # Very Clean solution from lee215. Time and Space: O(N)
    def insert(self, intervals, newInterval):
        s, e = newInterval
        parts = merge, left, right = [], [], []
        for i in intervals:
            # Very pyhonic. 
            # 0 when both are False, 
            # 1 when left is correct, 
            # -1 when right is correct. 
            parts[(i[-1] < s) - (i[0] > e)].append(i) 
        if merge:
            s = min(s, merge[0][0])
            e = max(e, merge[-1][-1])
        return left + [[s, e]] + right
    
    # Very Clean solution from lee215. Time and Space: O(N)
    def insert(self, intervals, newInterval):
        s, e = newInterval
        left = [i for i in intervals if i[-1] < s]
        right = [i for i in intervals if i[0] > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[~len(right)][-1])
        return left + [[s, e]] + right
            
# @lc code=end

