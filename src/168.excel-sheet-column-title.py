#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
# TAGS: Math
# REVIEWME: Math Trick


class Solution:
    # 28 ms, 74.42%. Time and Space: O(logN)
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber:
            columnNumber, r = divmod(columnNumber, 26)
            # This pattern occurs a lot when we want to deal with edge case.
            # which can be fixed in easily in the second solution
            if r == 0:
                r = 26
                columnNumber -= 1
            ans.append(chr(r + ord('A') - 1))
        return "".join(reversed(ans))

    # 28 ms, 74.42%. Time and Space: O(logN)
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber:
            # Fix with columnNumber - 1
            columnNumber, r = divmod(columnNumber - 1, 26)
            ans.append(chr(r + ord('A')))
        return "".join(reversed(ans))
# @lc code=end
