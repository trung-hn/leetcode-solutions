#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#

# @lc code=start
# TAGS: Array, Math
# REVIEWME: Math


class Solution:
    """
    Approach:
    First sol: try all combinations that are % 60
    Second sol: because this is modulo,
    we can keep track of only val % 60
    """
    # 452 ms, 5.02%. Time and Space: O(N)

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        divisible_by_60 = list(range(60, 501, 60))
        ans = 0
        visited = collections.defaultdict(int)
        for t in time:
            for d in divisible_by_60:
                ans += visited[d - t]
            visited[t] += 1
        return ans

    # 236 ms, 47.49%. Time: O(N) Space: O(1)
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        visited = [0] * 60
        for t in time:
            if t % 60 == 0:
                ans += visited[0]
            else:
                ans += visited[60 - t % 60]
            visited[t % 60] += 1
        return ans
# @lc code=end
