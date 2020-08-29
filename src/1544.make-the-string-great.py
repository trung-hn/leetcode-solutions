#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#

# @lc code=start
# TAGS: String, Stack
class Solution:
    # 32 ms, 90.71 %. Time and Space: O(N)
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if stack \
            and c != stack[-1] \
            and c.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
        
# @lc code=end

