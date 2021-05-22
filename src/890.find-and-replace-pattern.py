#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#

# @lc code=start
# TAGS: String


class Solution:
    """
    Approach:
    Convert other strings to the same plane:
    letter appear 1st is converted to "a"
    letter appear 2nd is converted to "b"
    ...
    in the second solution, we convert to number instead:
    0 means "a"
    1 means "b"

    Time and Space: O(N*K)
    """
    # 28 ms, 82%. Create our own hash for dictionary

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def get_hash(word):
            D = {}
            res = []
            for c in word:
                if c not in D:
                    D[c] = str(len(D) + 1)
                res.append(D[c])
            return "".join(res)
        pattern = get_hash(pattern)
        return [w for w in words if get_hash(w) == pattern]

    # 24 ms, 94%. Pythonic. No need to convert to string. keep it as tuple.
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def get_hash(word):
            D = {}
            return tuple(D.setdefault(c, len(D)) for c in word)
        pattern = get_hash(pattern)
        return [w for w in words if get_hash(w) == pattern]
# @lc code=end
