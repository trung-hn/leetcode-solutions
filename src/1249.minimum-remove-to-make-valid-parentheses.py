#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
# TAGS: Stack, String
class Solution:
    # 120 ms, 65.25%. Time: O(N). Space: O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove = set()
        close_parens = []
        op = 0
        for i, c in enumerate(s):
            if c == "(":
                op += 1
                close_parens.append(i)
            elif c == ")":
                op -= 1
            if op < 0:
                to_remove.add(i)
                op += 1
        if op:
            for val in close_parens[-op:]:
                to_remove.add(val)

        return "".join(c for i, c in enumerate(s) if i not in to_remove)
         

# @lc code=end

