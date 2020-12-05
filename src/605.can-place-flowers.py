#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start
# TAGS: Array, Greedy
class Solution:
    # 184 ms, 10.86%. Time: O(N). Space: O(1)
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            v1 = flowerbed[i - 1] if i else 0
            v2 = flowerbed[i]
            v3 = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
            if v1 == v2 == v3 == 0:
                flowerbed[i] = 1
                cnt += 1
        return cnt >= n
# @lc code=end

