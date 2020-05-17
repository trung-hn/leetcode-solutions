#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#
# TAGS: String
# REVIEWME:
# @lc code=start
class Solution:
    # 40 ms, O(N), O(1)
    def maxPower(self, s: str) -> int:
        s += "."
        char = s[0]
        power = rv = 1
        for c in s[1:]:
            if char is None or char == c:
                power += 1
            else:
                rv = max(rv, power)
                power = 1
            char = c
        return rv

    # 44 ms
    def maxPower(self, s: str) -> int:
        char = None
        power = rv = 1
        for c in s:
            if char == c:
                power += 1
            else:
                power = 1
                char = c
            rv = max(rv, power)
        return rv

# @lc code=end

