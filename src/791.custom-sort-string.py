#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
# TAGS: String
import string
import collections


class Solution:
    # 28 ms, 80.98%. Time and Space: O(N). N = len(T)
    def customSortString(self, S: str, T: str) -> str:
        counter = collections.Counter(T)
        ans = []
        for c in S:
            ans.append(c * counter[c])

        for c in set(string.ascii_lowercase) - set(S):
            ans.append(c * counter[c])

        return ''.join(ans)
# @lc code=end
