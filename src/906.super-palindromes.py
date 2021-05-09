#
# @lc app=leetcode id=906 lang=python3
#
# [906] Super Palindromes
#

# @lc code=start
# TAGS: Math


class Solution:
    """
    Approach:
    We can create a palindromic string from a number by:
    number + reversed(number) and then check its square
    With this, we reduce the complexity to just 1/4 length of right
    """
    # Time and Space: Complex

    def superpalindromesInRange(self, left: str, right: str) -> int:
        def is_valid(n):
            sqr = int(n) ** 2
            if left <= sqr <= right:
                sqr = str(sqr)
                return sqr == sqr[::-1]
            return False

        left = int(left)
        right_l = len(right)
        right = int(right)
        total = 0
        for n in range(1, 10**(right_l // 4 + 1)):
            n = str(n)
            total += is_valid(n + n[:-1][::-1])
            total += is_valid(n + n[::-1])
        return total

# @lc code=end
