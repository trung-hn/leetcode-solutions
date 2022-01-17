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
            swaps = sum(v1 != v2 for v1, v2 in zip(s, t))
            return float(inf) if swaps % 2 else swaps // 2

        ones = s.count('1')
        zeroes = s.count('0')
        if abs(ones - zeroes) > 1:
            return -1

        return min(compare(s, "10" * max(ones, zeroes)),
                   compare(s, "01" * max(ones, zeroes)))

# @lc code=end
