#
# @lc app=leetcode id=1864 lang=python3
#
# [1864] Minimum Number of Swaps to Make the Binary String Alternating
#

# @lc code=start
# TAGS: String, Greedy
class Solution:
    # 24 ms, 99.55%. Time and Space: O(N)
    def minSwaps(self, s: str) -> int:

        def compare(s, t):
            return sum(v1 != v2 for v1, v2 in zip(s, t)) // 2

        ones = s.count('1')
        zeroes = s.count('0')
        if abs(ones - zeroes) > 1:
            return -1

        rv = float("inf")
        if ones > zeroes:
            rv = min(rv, compare(s, "10" * zeroes + "1"))
        elif zeroes > ones:
            rv = min(rv, compare(s, "01" * ones + "0"))
        else:
            rv = min(rv, compare(s, "10" * ones))
            rv = min(rv, compare(s, "01" * ones))
        return rv

# @lc code=end
