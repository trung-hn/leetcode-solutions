#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
# TAGS: Array
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        seenAB = collections.defaultdict(int)
        for a in A:
            for b in B:
                seenAB[a + b] += 1
        for c in C:
            for d in D:
                ans += seenAB[-c-d]
        return ans
# @lc code=end

