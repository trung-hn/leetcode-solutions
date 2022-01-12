#
# @lc app=leetcode id=2085 lang=python3
#
# [2085] Count Common Words With One Occurrence
#

# @lc code=start
import collections
from typing import List


class Solution:
    # 105 ms, 30.70%. Time and Space: O(N)
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        c1 = collections.Counter(words1)
        c2 = collections.Counter(words2)
        ans = 0
        for k in c1:
            if c1[k] == c2[k] == 1:
                ans += 1
        return ans
# @lc code=end
