#
# @lc app=leetcode id=3106 lang=python3
#
# [3106] Lexicographically Smallest String After Operations With Constraint
#


# @lc code=start
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def get_new_c(c, dist):
            if ord(c) + dist > ord("z"):
                return "a"
            if ord(c) - dist <= ord("a"):
                return "a"
            if ord(c) - dist > ord("a"):
                return chr(ord(c) - dist)

        def dist(c1, c2):
            return min(ord(c) - ord(c1), ord(c1) + 26 - ord(c2))

        ans = []
        for c in s:
            new_c = get_new_c(c, k)
            ans.append(new_c)
            k -= dist(new_c, c)
        return "".join(ans)


# @lc code=end
