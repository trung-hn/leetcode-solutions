#
# @lc app=leetcode id=1529 lang=python3
#
# [1529] Bulb Switcher IV
#

# @lc code=start
# TAGS: String
class Solution:
    # 116 ms, 49.82 %. Time: O(N). Space: O(1)
    def minFlips(self, target: str) -> int:
        cnt = int(target[0])
        for b1, b2 in zip(target, target[1:]):
            if b1 != b2: cnt += 1
        return cnt

        
# @lc code=end