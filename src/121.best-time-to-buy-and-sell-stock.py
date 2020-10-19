#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
# TAGS: Dynamic Programming
class Solution:
    # 60 ms, 84.22% Greedy. Time: O(N). Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        start = prices[0]
        total = 0
        for price in prices[1:]:
            if price < start:
                start = price
            else:
                total = max(total, price - start)
        return total

    # DP. Time: O(N). Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        max_total = max_cur = 0
        for i in range(1, len(prices)):
            max_cur = max(0, max_cur + prices[i] - prices[i - 1])
            max_total = max(max_total, max_cur)
        return max_total
# @lc code=end

