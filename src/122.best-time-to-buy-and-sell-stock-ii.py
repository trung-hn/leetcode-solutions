#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
# TAGS: Array, Greedy
class Solution:
    # DP
    def maxProfit(self, prices: List[int]) -> int:
        max_total = max_cur = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i - 1]<0:
                max_total += max_cur
                max_cur = 0
            else:
                max_cur += prices[i] - prices[i - 1]
        return max_total + max_cur
    
    # Greedy. 48 ms, 99.56%. Greedy
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        start = prices[0]
        for price in prices[1:]:
            if price > start:
                total += price - start
            start = price
        return total
    
# @lc code=end

