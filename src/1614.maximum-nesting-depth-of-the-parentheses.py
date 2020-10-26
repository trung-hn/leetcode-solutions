#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#

# @lc code=start
# TAGS: String
class Solution:
    # 24 ms, 94.84%. Time: O(N). Space: O(1)
    def maxDepth(self, s: str) -> int:
        op = ans = 0
        for c in s:
            if c == '(':
                op += 1
            elif c == ')':
                op -= 1
            ans = max(ans, op)
        return ans
# @lc code=end

