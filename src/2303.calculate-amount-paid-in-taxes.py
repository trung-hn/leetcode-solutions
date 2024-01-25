#
# @lc app=leetcode id=2303 lang=python3
#
# [2303] Calculate Amount Paid in Taxes
#


# @lc code=start
# TAGS: Array, Simulation
class Solution:
    # Time: O(N). Space: O(1)
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = prev_upper = 0
        for upper, tax in brackets:
            amount = min(income, upper - prev_upper)
            ans += amount * tax
            prev_upper = upper
            income -= amount
            if income == 0:
                break
        return ans / 100


# @lc code=end
