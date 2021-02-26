#
# @lc app=leetcode id=946 lang=python3
#
# [946] Validate Stack Sequences
#

# @lc code=start
# TAGS: Stack
class Solution:
    # 64 ms, 94.09%. Time and Space: O(N)
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ptr = 0
        stack = []
        for val in pushed:
            stack.append(val)
            while stack and stack[-1] == popped[ptr]:
                ptr += 1
                stack.pop()
        return stack == []
            
# @lc code=end

