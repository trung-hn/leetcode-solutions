#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#

# @lc code=start


class Solution:
    """
    Approach: Just sort the array
    """
    # 968 ms, 100%. Time: O(NlogN)

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0
        for i, cost in enumerate(costs):
            total += cost
            if total > coins:
                return i
        return len(costs)
# @lc code=end
