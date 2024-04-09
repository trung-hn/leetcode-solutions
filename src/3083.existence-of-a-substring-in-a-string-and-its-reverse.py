#
# @lc app=leetcode id=3083 lang=python3
#
# [3083] Existence of a Substring in a String and Its Reverse
#


# @lc code=start
# TAGS: Hash Table, String
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        seen = set()
        for c1, c2 in zip(s, s[1:]):
            if c1 == c2 or (c1, c2) in seen:
                return True
            seen.add((c2, c1))
        return False


# @lc code=end
