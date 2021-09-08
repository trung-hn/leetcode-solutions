#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#

# @lc code=start
# TAGS: Array, String


class Solution:
    # 200 ms, 63.61%. Time and Space: O(N)
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        ans = []
        shift = 0
        for i in range(len(shifts)):
            shift = (shift + shifts[~i]) % 26
            ans.append(chr(97 + (ord(S[~i]) - 97 + shift) % 26))
        return "".join(reversed(ans))

# @lc code=end
