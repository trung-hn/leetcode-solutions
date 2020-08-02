#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    # 24 ms, 95.83%. Time O(N) Space O(1)
    def detectCapitalUse(self, word: str) -> bool:
        return word in (word.lower(), word.upper(), word.capitalize())

    # 24 ms, 95.83%. Time O(N) Space O(1)
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() or word.isupper() or word.istitle()
        
# @lc code=end

