#
# @lc app=leetcode id=3084 lang=python3
#
# [3084] Count Substrings Starting and Ending with Given Character
#


# @lc code=start
class Solution:
    # Time: O(N). Space: O(1)
    def countSubstrings(self, s: str, c: str) -> int:
        n = s.count(c)
        return (n + 1) * n // 2


# @lc code=end
