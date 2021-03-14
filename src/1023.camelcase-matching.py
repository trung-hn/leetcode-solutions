#
# @lc app=leetcode id=1023 lang=python3
#
# [1023] Camelcase Matching
#

# @lc code=start
# TAGS: String, Trie
# REVIEWME: Pythonic


class Solution:
    # 32 ms, 73.14%. Time: O(Q*N). Space: O(Q). Q = len(queries). N = len(query)
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(q, p):
            i = j = 0
            while i < len(q):
                if j < len(p) and q[i] == p[j]:
                    j += 1
                elif q[i].isupper():
                    return False
                i += 1
            return j == len(p)
        return [match(q, pattern) for q in queries]

    # Pythonic solution from lee215
    def camelMatch(self, queries: List[str], p: str) -> List[bool]:
        def uppers(s):
            return [c for c in s if c.isupper()]

        def is_within(q, p):
            it = iter(q)
            return all(c in it for c in p)

        return [uppers(q) == uppers(p) and is_within(q, p) for q in queries]
# @lc code=end
