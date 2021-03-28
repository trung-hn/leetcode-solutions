#
# @lc app=leetcode id=423 lang=python3
#
# [423] Reconstruct Original Digits from English
#

# @lc code=start
# TAGS: Math


class Solution:
    # 32 ms, 99.40%. Time and Space: O(N)
    def originalDigits(self, s: str) -> str:
        match = [(0, "z", "ero"), (2, "w", "to"), (4, "u", "for"), (6, "x", "si"), (8, "g", "eiht"),
                 (1, "o", "ne"), (3, "t", "hree"), (5, "f", "ive"), (7, "s", "even"),  (9, "i", "nne")]

        counter = collections.Counter(s)
        freq = [0] * 10
        for n, key, rest in match:
            cnt = counter[key]
            for c in rest:
                counter[c] -= cnt
            freq[n] += cnt
            counter[key] = 0

        return "".join(str(i) * val for i, val in enumerate(freq))
# @lc code=end
