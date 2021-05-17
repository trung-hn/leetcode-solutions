#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
# TAGS: String


class Solution:
    # 32 ms, 68.53%. Time and Space: O(N)
    def replaceDigits(self, s: str) -> str:
        ans = []
        for i, c in enumerate(s):
            if i % 2:
                ans.append(chr(ord(s[i - 1]) + int(c)))
            else:
                ans.append(c)
        return "".join(ans)
# @lc code=end
