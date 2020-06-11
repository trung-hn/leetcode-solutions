#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
# TAGS: Bit Manipulation
# REVIEWME: important technique in bitwise manipulation
class Solution:
    # Naive solution. Time O(log N), Space O(1)
    def isPowerOfTwo(self, n: int) -> bool:
        while n:
            if n == 1:
                return True
            elif n % 2:
                return False
            n /= 2
        return False

    # Better solution. Turn off right most bit and compare with 0
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0
# @lc code=end

