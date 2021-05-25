#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
# TAGS: Stack


class Solution:
    # 60 ms, 92.42%. Time and Space: O(N)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                stack.append(- stack.pop() + stack.pop())
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                temp = stack.pop()
                stack.append(int(stack.pop() / temp))
            else:
                stack.append(int(token))
        return stack.pop()
# @lc code=end
