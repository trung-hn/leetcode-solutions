#
# @lc app=leetcode id=1239 lang=python3
#
# [1239] Maximum Length of a Concatenated String with Unique Characters
#

# @lc code=start
# TAGS: Backtracking, Bit Manipulation


class Solution:
    # 84 ms, 92.06%. Time: O(2^N). Space: O(N)
    def maxLength(self, arr: List[str]) -> int:
        chars = [set(s) for s in arr if len(s) == len(set(s))]

        def dfs(i=0, seen=set()):
            if i == len(chars):
                return len(seen)
            # Don't include this
            skip = dfs(i + 1, seen)
            if seen & chars[i]:
                return skip
            # Include this
            take = dfs(i + 1, seen | chars[i])
            return max(skip, take)

        return dfs() if chars else 0
# @lc code=end
