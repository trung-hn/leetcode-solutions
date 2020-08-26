#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
# TAGS: Greedy, Simulation
class Solution:
    # 32 ms, 73.93 %. Time: O(logN). Space: O(1)
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0
        emptyBottles = 0
        while numBottles:
            total += numBottles
            numBottles += emptyBottles
            numBottles, emptyBottles = divmod(numBottles, numExchange)
        return total

    # 24 ms, 96.22%. Time and Space: O(1). 
    # From discussion: https://leetcode.com/problems/water-bottles/discuss/745231/Python-1-liner-with-math-explained
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)

# @lc code=end