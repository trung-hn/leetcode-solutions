#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
# TAGS: Binary Search, Dynamic Programming
# REVIEWME: Binary Search, Dynamic Programming
import bisect


class Solution:
    # Base on discussion
    # 140 ms, 96.79%. Time: O(NlogN). Space: O(N)
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        lis = []
        for _, e in envelopes:
            i = bisect.bisect_left(lis, e)
            lis[i: i+1] = [e]
        return len(lis)
# @lc code=end
