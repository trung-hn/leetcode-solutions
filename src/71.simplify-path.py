#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
# TAGS: String, Stack
class Solution:
    # 28 ms, 89.90%. Time and Space: O(N)
    def simplifyPath(self, path: str) -> str:
        stack = []
        for pos in path.split("/"):
            if not pos: continue
            if pos == ".": continue
            if pos == "..":
                if stack: stack.pop()
            else:
                stack.append(pos)
        return "/" + "/".join(stack)
# @lc code=end

