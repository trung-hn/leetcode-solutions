#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# TAGS: String, Stack
# @lc code=start
class Solution:
    # time complexity: O(N). N = len(s)
    # Space complexity: O(N). N = len(s)
    # Other ways: Use map, constant space 
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if len(stack):
                if (c == ")" and stack[-1] == "(") \
                or (c == "]" and stack[-1] == "[") \
                or (c == "}" and stack[-1] == "{"):
                    stack.pop()
                    continue
            stack.append(c)
        return len(stack) == 0

# @lc code=end