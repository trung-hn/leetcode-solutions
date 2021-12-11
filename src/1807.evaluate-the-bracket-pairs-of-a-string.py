#
# @lc app=leetcode id=1807 lang=python3
#
# [1807] Evaluate the Bracket Pairs of a String
#

# @lc code=start
# TAGS: Array, Hash Table, String
from typing import List
from collections import defaultdict


class Solution:
    # 952 ms, 70.53%. Time and Space: O(N)
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        known = defaultdict(lambda: "?", knowledge)
        rv = []
        curr = ""
        for c in s:
            if c == ")":
                rv.append(known[curr[1:]])
                curr = ""
            elif c == "(" or curr:
                curr += c
            else:
                rv.append(c)
        return "".join(rv)

    # 932 ms, 85.26%. Time and Space: O(N)
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        known = defaultdict(lambda: "?", knowledge)
        splits = s.split("(")
        rv = [splits[0]]
        for sp in splits[1:]:
            key, rest = sp.split(")")
            rv.extend([known[key], rest])
        return "".join(rv)
# @lc code=end
