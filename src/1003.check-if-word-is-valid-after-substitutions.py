#
# @lc app=leetcode id=1003 lang=python3
#
# [1003] Check If Word Is Valid After Substitutions
#

# @lc code=start
# TAGS: String, Stack
class Solution:
    # 88 ms, 37.74%. Time: O(N). Space: O(N)
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            stack.append(c)
            if c == "c" and len(stack) >= 3:
                if stack[-3:] == ['a', 'b', 'c']:
                    stack.pop(); stack.pop(); stack.pop()
        return len(stack) == 0
# @lc code=end

