#
# @lc app=leetcode id=830 lang=python3
#
# [830] Positions of Large Groups
#

# @lc code=start
class Solution:
    # 36 ms, 75.04 %. O(N).
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        rv = []
        cnt = 1
        S += "."
        for i in range(len(S) - 1):
            a, b = S[i], S[i + 1]
            if a == b:
                cnt += 1
            else:
                if cnt >= 3:
                    rv.append([i - cnt + 1, i])
                cnt = 1
        return rv

# @lc code=end

