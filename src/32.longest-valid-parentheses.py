#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
# TAGS: String, Dynamic Programming


class Solution:
    # 40 ms, 80%. Time and Space: O(N)
    def longestValidParentheses(self, s: str) -> int:
        max_cnt = cnt = 0
        stack = []
        for c in s:
            if c == "(":
                stack.append(cnt)
                cnt = 0
            else:
                if stack:
                    cnt += 2 + stack.pop()
                else:
                    cnt = 0
            max_cnt = max(max_cnt, cnt)
        return max_cnt

# @lc code=end
