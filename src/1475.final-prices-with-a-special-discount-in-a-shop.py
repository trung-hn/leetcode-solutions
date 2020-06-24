#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start
# TAGS: Monotonic Stack
class Solution:

    # Bruteforce. 56 ms, 75.95%. O(N^2), O(1)
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
        return prices

    # Optimal solution. 48 ms, 95.17%. O(N), O(1)
    def finalPrices(self, prices: List[int]) -> List[int]:
        monotonic_stack = []
        for i, price in enumerate(prices):
            while monotonic_stack and prices[monotonic_stack[-1]] >= price:
                prices[monotonic_stack.pop()] -= price
            monotonic_stack.append(i)
        return prices

# @lc code=end

