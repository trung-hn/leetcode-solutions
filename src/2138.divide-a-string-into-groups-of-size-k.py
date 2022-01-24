#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
# TAGS: String, Simulation
from typing import List


class Solution:
    # 52 ms, 32.9%. Time and Space: O(N)
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(0, len(s), k):
            ans.append(s[i: i + k])

        ans[-1] += fill * (k - len(ans[-1]))
        return ans
# @lc code=end
