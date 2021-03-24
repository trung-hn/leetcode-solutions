#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
# TAGS: Array, Two Pointers, Dynamic Programming, Stack


class Solution:
    # There is a better solution that built from DP with Space O(1)
    # 48 ms, 93.07%. DP. Time and Space: O(N). N = len(height)
    def trap(self, height: List[int]) -> int:
        left = [0]
        for h in height:
            left.append(max(left[-1], h))

        right = [0]
        for h in reversed(height):
            right.append(max(right[-1], h))
        right.reverse()

        total = 0
        for wl, wr, h in zip(left, right[1:], height):
            wall = min(wl, wr)
            if wall > h:
                total += wall - h
        return total
# @lc code=end
