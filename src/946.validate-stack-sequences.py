#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
# TAGS: Stack
class Solution:
    # 68 ms, 85.45%. Time and Space: O(N)
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = j = 0
        stack = []
        while i < len(pushed):
            stack.append(pushed[i])
            while stack and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            i += 1
        return not stack
# @lc code=end

