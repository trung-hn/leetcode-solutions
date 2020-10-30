#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
# TAGS: Stack, DFS
# REVIEWME: Stack, DFS
class Solution:
    # 32 ms. 41.14%. Time: O(maxK*N), Space: O(N). K is the multiplier
    def decodeString(self, s: str) -> str:
        
        def recurse(s):
            op = 0; ptr = num = None; rv = []
            for i in range(len(s)):
                if s[i].isdigit():
                    if num is None: num = i
                elif s[i] == "[":
                    if ptr is None: ptr = i
                    op += 1
                elif s[i] == "]":
                    op -= 1
                    if op == 0:
                        rv.append(int("".join(s[num : ptr])) * recurse(s[ptr + 1 : i]))
                        ptr = num = None
                elif not op:
                    rv.append(s[i])
            return "".join(rv)
        return recurse(s)

    # 28 ms, 73.98%. 
    # From discussion: https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
    def decodeString(self, s: str) -> str:
        stack = []; cur_num = 0; curr_string = ''
        for c in s:
            if c == "[":
                stack.extend([curr_string, cur_num])
                cur_num = 0; curr_string = ''
            elif c == "]":
                num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + num * curr_string
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                curr_string += c
        return curr_string
# @lc code=end

