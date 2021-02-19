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
                if op == 0:
                    to_remove.add(i)
                    continue
                op -= 1
        if op: to_remove |= set(close_parens[-op:])
        return "".join(c for i, c in enumerate(s) if i not in to_remove)

    # Same idea but slightly cleaner         
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack: stack.pop()
                else: s[i] = ""
        for i in stack: s[i] = ""
        return "".join(s)

# @lc code=end

