#
# @lc app=leetcode id=1812 lang=python3
#
# [1812] Determine Color of a Chessboard Square
#

# @lc code=start
# TAGS: Math, String
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        r, c = coordinates
        r = ord(r) - ord('a')
        c = int(c) - 1
        return (r + c) % 2
# @lc code=end
