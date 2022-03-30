#
# @lc app=leetcode id=2180 lang=python3
#
# [2180] Count Integers With Even Digit Sum
#

# @lc code=start
# TAGS: Math, Simulation
class Solution:
    def countEven(self, num: int) -> int:
        cnt = 0
        for i in range(1, num + 1):
            cnt += sum(int(c) for c in str(i)) % 2 == 0
        return cnt

    # Math
    # For a num with even sum of its digits, count of Integers With Even Digit Sum less than or equal to num is num/2
    # For a num with odd sum of its digits, count of Integers With Even Digit Sum less than or equal to num is (num-1)/2
    # Time and Space: O(1)
    def countEven1(self, num: int) -> int:
        if sum(int(c) for c in str(num)) % 2:
            return (num - 1) // 2
        return num // 2

# @lc code=end
