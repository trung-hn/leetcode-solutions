#
# @lc app=leetcode id=2186 lang=python3
#
# [2186] Minimum Number of Steps to Make Two Strings Anagram II
#

# @lc code=start
# TAGS: Hash Table, String, Counting
import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        return sum((c1 - c2).values()) + sum((c2 - c1).values())

# @lc code=end
