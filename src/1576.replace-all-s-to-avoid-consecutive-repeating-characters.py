#
# @lc app=leetcode id=1576 lang=python3
#
# [1576] Replace All ?'s to Avoid Consecutive Repeating Characters
#

# @lc code=start
# TAGS: String
import string
class Solution:
    # 36 ms, 48.67 %. Time: O(N*26). Space: O(N). We only need 3 characters to make repeating sequence. 
    def modifyString(self, s: str) -> str:
        ans = []
        for i, c in enumerate(s):
            if c == "?":
                forbidden = set()
                if i: forbidden.add(ans[-1])
                if i < len(s) - 1: forbidden.add(s[i + 1])
                ans.append(({'a', 'b', 'c'} - forbidden).pop())
            else:
                ans.append(c)
        return "".join(ans)
# @lc code=end

