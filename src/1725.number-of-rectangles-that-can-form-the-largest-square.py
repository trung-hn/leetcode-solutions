#
# @lc app=leetcode id=1725 lang=python3
#
# [1725] Number Of Rectangles That Can Form The Largest Square
#

# @lc code=start
# TAGS: Greedy
class Solution:
    # 172 ms, 99.41%. Time: O(N). Space: O(1)
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_size = 0
        cnt = 0
        for rectangle in rectangles:
            temp = min(rectangle)
            if temp == max_size:
                cnt += 1
            elif temp > max_size:
                max_size = temp
                cnt = 1
        return cnt
# @lc code=end

