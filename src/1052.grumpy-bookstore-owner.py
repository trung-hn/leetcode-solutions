#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
# TAGS: Sliding Window, Array


class Solution:
    # 292 ms, 56.63%. Time and Space: O(N)
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        angry = [cust if mood else 0 for cust, mood in zip(customers, grumpy)]

        # Sliding Window
        total = max_sofar = 0
        for i, cust in enumerate(angry):
            total += cust
            if max_sofar < total:
                max_sofar = total
            if i >= X - 1:
                total -= angry[i - X + 1]
        return max_sofar + sum(cust for cust, mood in zip(customers, grumpy) if not mood)


# @lc code=end
