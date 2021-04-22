#
# @lc app=leetcode id=1816 lang=python3
#
# [1816] Truncate Sentence
#

# @lc code=start


class Solution:
    # 28 ms, 84.68%. Time: O(N). Space: O(1)
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split(" ", k)[:k])
# @lc code=end
