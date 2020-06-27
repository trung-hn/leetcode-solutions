#
# @lc app=leetcode id=1481 lang=python3
#
# [1481] Least Number of Unique Integers after K Removals
#

# @lc code=start
# TAGS: Array, Sort
class Solution:
    # 464 ms, 96.27%. Time: O(NlogN), Time: O(N)
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = collections.Counter(arr)
        freqs = sorted(freq.values())
        accum = itertools.accumulate(freqs)
        for i, val in enumerate(accum, 1):
            if val == k: return len(freqs) - i
            elif val > k: return len(freqs) - (i - 1)
        return 0

# @lc code=end

