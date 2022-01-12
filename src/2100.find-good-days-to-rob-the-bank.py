#
# @lc app=leetcode id=2100 lang=python3
#
# [2100] Find Good Days to Rob the Bank
#

# @lc code=start
# TAGS: Array, Dynamic Programming, Prefix Sum
from typing import List


class Solution:
    # 1131 ms. 41.74%. Time and Space: O(N)
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:

        prefix = [0]
        suffix = [0]
        for i in range(1, len(security)):
            v1, v2 = security[i - 1], security[i]
            v3, v4 = security[~i], security[-i]
            prefix.append(prefix[-1] + 1 if v1 >= v2 else 0)
            suffix.append(suffix[-1] + 1 if v3 <= v4 else 0)

        return [i for i in range(len(prefix))
                if prefix[i] >= time and suffix[~i] >= time]


# @lc code=end
