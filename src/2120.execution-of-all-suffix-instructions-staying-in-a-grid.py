#
# @lc app=leetcode id=2120 lang=python3
#
# [2120] Execution of All Suffix Instructions Staying in a Grid
#

# @lc code=start
# TAGS: String, Simulation

from typing import List


class Solution:
    # 1316 ms, 83.84%. Time and Space: O(S)
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        delta = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
        ans = []
        for start in range(len(s)):
            r, c = startPos
            cnt = start
            for d in s[start:]:
                delta_r, delta_y = delta[d]
                r += delta_r
                c += delta_y
                if not (0 <= r < n and 0 <= c < n):
                    break
                cnt += 1
            ans.append(cnt - start)
        return ans
# @lc code=end
