#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
# TAGS: String
# REVIEWME: String


class Solution:
    """
    Approach: get min count of 0s and 1s at the intersections of 0s and 1s
    """
    # 184 ms, 47%. Time O(N). Space O(N). Pythonic

    def countBinarySubstrings(self, s: str) -> int:
        groups = [len(list(g)) for _, g in itertools.groupby(s)]
        return sum(min(g1, g2) for g1, g2 in zip(groups, groups[1:]))

    # 112 ms, 97%. Time O(N). Space O(1). 1 pass
    def countBinarySubstrings(self, s: str) -> int:
        init = s[0]
        prev, cur = 0, 1
        ans = 0
        for c in s[1:]:
            if c == init:
                cur += 1
            else:
                ans += min(prev, cur)
                prev, cur = cur, 1
                init = c
        return ans + min(prev, cur)
# @lc code=end
