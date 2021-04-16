#
# @lc app=leetcode id=1209 lang=python3
#
# [1209] Remove All Adjacent Duplicates in String II
#

# @lc code=start
# TAGS: Stack


class Solution:
    # 40 ms, 96.60%. Time and Space: O(N)
    def removeDuplicates(self, s: str, k: int) -> str:
        char = ""
        cnt = 0
        stack = []
        for c in s + ".":
            # Running counter of current char
            if c == char:
                cnt += 1
                continue

            # if prev_char is the same, combine cnt
            if stack and stack[-1][0] == char:
                cnt += stack.pop()[1]

            # Add remainder to stack
            if cnt % k:
                stack.append((char, cnt % k))

            # Reset counter
            char = c
            cnt = 1
        return "".join(char * cnt for char, cnt in stack)
# @lc code=end
