#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

# @lc code=start
# TAGS: Greedy
class Solution:
    # 144 ms, 64.42%. Time: O(N) Space: O(1)
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = collections.Counter(word1)
        c2 = collections.Counter(word2)
        c1_val = collections.Counter(c1.values())
        c2_val = collections.Counter(c2.values())
        return c1_val == c2_val and set(word1) == set(word2)
# @lc code=end

