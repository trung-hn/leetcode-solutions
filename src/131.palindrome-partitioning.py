#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
# TAGS: String, Dynamic Programming, Backtracking
from typing import List


class Solution:
    # Time: O(N*2^N). Space: O(N)
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            L = len(s)
            return all(s[i] == s[~i] for i in range(L//2))

        def dfs(start=0, sofar=[]):
            if start == len(s):
                ans.append([val for val in sofar])
                return

            for end in range(start, len(s)):
                sub = s[start: end + 1]
                if is_palindrome(sub):
                    sofar.append(sub)
                    dfs(end + 1, sofar)
                    sofar.pop()
        ans = []
        dfs()
        return ans
# @lc code=end
