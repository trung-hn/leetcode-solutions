#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#

# @lc code=start
# TAGS: Greedy
# REVIEWME: Tricky problem, very nice solution
class Solution:
    # 40 ms, 47%. O(NlogN) because of sorting. 
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # A-B is the money lost by sending a person to A. We want this to be as small as possible (negative).
        costs.sort(key=lambda x: x[0] - x[1])
        total = 0
        for i in range(len(costs)):
            a, b = costs[i]
            if i < len(costs)/2:
                total += a
            else:
                total += b
        return total
    
    # 36 ms, 80%. O(NlogN). Pythonic
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        N = len(costs)//2
        return sum(costs[i][0] + costs[i+N][1] for i in range(N)) 
# @lc code=end

