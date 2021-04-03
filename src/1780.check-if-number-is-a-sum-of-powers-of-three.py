#
# @lc app=leetcode id=1780 lang=python3
#
# [1780] Check if Number is a Sum of Powers of Three
#

# @lc code=start
# TAGS: Math, Backtracking, Recursion


class Solution:
    # 396 ms, 22.41%. Time: O(N). Space: O(N).
    def checkPowersOfThree(self, n: int) -> bool:
        powers = [3**i for i in range(20) if 3**i <= n]

        def dp(start, total):
            if total == 0:
                return True
            if start == len(powers) or total < 0:
                return False
            skip = dp(start + 1, total)
            take = dp(start + 1, total - powers[start])
            return skip or take
        return dp(0, n)

    # Math solution from discussion. Time: O(logN). Space: O(1)
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 1:
            n, r = divmod(n, 3)
            if r == 2:
                return False
        return True

# @lc code=end
