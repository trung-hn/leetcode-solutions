#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
# TAGS: String
class Solution:
    # 272 ms, 36.61%. Time: O(N). Space: O(1)
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        base = set(allowed)
        return sum(not bool(set(word) - base) for word in words)

# @lc code=end

