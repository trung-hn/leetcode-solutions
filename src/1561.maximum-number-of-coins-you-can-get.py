#
# @lc app=leetcode id=1561 lang=python3
#
# [1561] Maximum Number of Coins You Can Get
#

# @lc code=start
# TAGS: Sort
class Solution:
    # 656 ms, 82.22 %. Time: O(NlogN) because of sorting. Space: O(1)
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles) // 3
        piles.sort(reverse=True)
        total = 0
        for i in range(n):
            total += piles[i*2 + 1]
        return total
# @lc code=end

