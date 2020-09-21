#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
# TAGS: Greedy
# REVIEWME: Bucket Sort. 
import collections
class Solution:
    # 52 ms, 99.61%. Time: O(N). Space: O(1). Bucket Sort
    # Not good if the value of miles is very large. 
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stations = [0] * 1000
        for i in range(len(trips)):
            no, start, end = trips[i]
            stations[start] += no
            stations[end] -= no
        
        total = 0
        for no in stations:
            total += no
            if total > capacity:
                return False
        return True


    # 52 ms, 99.61%. Time: O(NlogN). Space: O(N). Higher Time Complexity but works better in general. 
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stations = collections.defaultdict(int)
        for i in range(len(trips)):
            no, start, end = trips[i]
            stations[start] += no
            stations[end] -= no
        
        total = 0
        for station in sorted(stations.keys()):

            total += stations[station]
            if total > capacity:
                return False
        return True

# @lc code=end

