#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
#
# TAGS: String
# @lc code=start
class Solution:
    # 44 ms, 54.86%. O(N), O(1)
    def maxPower(self, s: str) -> int:
        cnt = ans = 1
        for c1, c2 in zip(s, s[1:]):
            if c1 == c2:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        return ans
# @lc code=end

