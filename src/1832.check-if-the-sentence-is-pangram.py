#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start


class Solution:
    # 56 ms, 100%. Time: O(N). Space: O(1)
    def checkIfPangram(self, sentence: str) -> bool:
        counters = [0] * 26
        for c in sentence:
            counters[ord(c) - ord('a')] += 1
        return 0 not in counters
# @lc code=end
