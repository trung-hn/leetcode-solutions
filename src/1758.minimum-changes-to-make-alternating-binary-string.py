#
# @lc app=leetcode id=1758 lang=python3
#
# [1758] Minimum Changes To Make Alternating Binary String
#

# @lc code=start
# TAGS: Array, Greedy


class Solution:
    # 44 ms, 96.73%. Time: O(N). Space: O(1)
    def minOperations(self, s: str) -> int:
        o1 = '1'
        o2 = '0'
        cnt1 = cnt2 = 0
        for c in s:
            if c != o1:
                cnt1 += 1
            if c != o2:
                cnt2 += 1
            o1 = '0' if o1 == '1' else '1'
            o2 = '0' if o2 == '1' else '1'
        return min(cnt1, cnt2)
# @lc code=end
