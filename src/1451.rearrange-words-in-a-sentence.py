#
# @lc app=leetcode id=1451 lang=python3
#
# [1451] Rearrange Words in a Sentence
#

# @lc code=start
# TAGS: String, Sort
class Solution:
    """
    56 ms, 75.95%. 
    Note that capitalize() will make the first character upper case and the rest lower case
    Time: O(N * logN) because of sorting
    Space: O(N)
    """
    def arrangeWords(self, text: str) -> str:
        return " ".join(sorted(text.split(), key=len)).capitalize()
# @lc code=end

