#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
# TAGS: String, Stack
class Solution:
    # 122 ms, 28.3%. Time and Space: O(N)
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        components = []; cur = 0
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            else:
                components.extend([cur, c])
                cur = 0
        components.append(cur)
        
        stack = []
        for val in components:
            if stack and stack[-1] == "*":
                stack.pop()
                stack.append(stack.pop() * val)
            elif stack and stack[-1] == "/":
                stack.pop()
                stack.append(int(stack.pop() / val))
            elif stack and stack[-1] == "-":
                stack.pop()
                stack.append(-val)
            elif stack and stack[-1] == "+":
                stack.pop()
                stack.append(val)
            else:
                stack.append(val)
        return sum(stack)
# @lc code=end

