#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start
# TAGS: Array, Math
class Solution:
    # 452 ms, 5.02%. Time and Space: O(N)
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        divisible_by_60 = list(range(60, 1001, 60))
        ans = 0
        visited = collections.defaultdict(int)
        for t in time:
            for d in divisible_by_60:
                ans += visited[d - t]
            visited[t] += 1
        return ans
    
    # 228 ms, 54.62%. Time: O(N) Space: O(1)
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        visited = collections.defaultdict(int)
        for t in time:
            if t % 60 == 0:
                ans += visited[0]
            else:
                ans += visited[60 - t % 60]
            visited[t % 60] += 1
        return ans
# @lc code=end

