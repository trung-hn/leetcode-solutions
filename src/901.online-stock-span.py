#
# @lc app=leetcode id=901 lang=python3
#
# [901] Online Stock Span
#

# @lc code=start
# TAGS: Monotonic Stack
# REVIEWME:
# 464 ms, 50%
class StockSpanner:
    # Time: O(1)
    def __init__(self):
        self.stack = []
    # Average Time: O(1)
    def next(self, price: int) -> int:
        total = 1
        while self.stack and self.stack[-1][0] <= price:
            total += self.stack.pop()[-1]
        self.stack.append((price, total))
        return total

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
# @lc code=end

