#
# @lc app=leetcode id=2038 lang=python3
#
# [2038] Remove Colored Pieces if Both Neighbors are the Same Color
#


# @lc code=start
# TAGS: Math, String, Greedy, Game Theory
class Solution:
    # 101 ms, 88.93%
    # Time: O(N). Space: O(1)
    def winnerOfGame(self, colors: str) -> bool:
        ans = cur = 0
        prev = "*"
        for color in colors + "*":
            if prev == color:
                cur += 1
            else:
                if prev == "A" and cur > 2:
                    ans += cur - 2
                elif prev == "B" and cur > 2:
                    ans -= cur - 2
                cur = 1
            prev = color
        return ans > 0


# @lc code=end
