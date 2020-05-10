#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#

# @lc code=start
# TAGS: Math, Tricky
class Solution:
    # TLE, Time: O(N^2)
    def bulbSwitch(self, n: int) -> int:
        bulbs = [1]*n
        for i in range(2, n + 1):
            temp = i
            while temp <= n:
                bulbs[temp - 1] += 1
                temp += i
        return sum(val % 2 for val in bulbs)

    # Optimal solution:
    # We only need to count number with odd number of operations:
    # Prime numbers will always be off (because of 1 and itself)
    # For normal numbers like 12: we have (1, 12), (2, 6), (3, 4) => It always come in pairs => off
    # For perfect square number like 16: we have (1, 16), (2, 8 ), (4, 4) => There is always an odd pair => on
    # from 1 to 16 there are 1 => sqrt(16) numbers => 4 bulbs
    # 20 ms, 98.11%. O(1), O(1)
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))
# @lc code=end

