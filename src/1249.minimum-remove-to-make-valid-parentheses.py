#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
# TAGS: Stack, String


class Solution:
    # 80 ms, 96.30%. Time and Space: O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        to_remove = []
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    to_remove.append(i)
        to_remove = set(to_remove + stack)
        return "".join(c for i, c in enumerate(s) if i not in to_remove)

    # 80 ms, 96.30%. Time and Space: O(N)
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ""
        for i in stack:
            s[i] = ""
        return "".join(s)

# @lc code=end
