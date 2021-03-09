#
# @lc app=leetcode id=789 lang=python3
#
# [789] Escape The Ghosts
#

# @lc code=start
# TAGS: Math


class Solution:
    # 36 ms, 100.00%. Time: O(N). Space: O(1)
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        dist_2_target = abs(target[0]) + abs(target[1])
        for x, y in ghosts:
            dist = abs(target[0] - x) + abs(target[1] - y)
            if dist <= dist_2_target:
                return False
        return True
# @lc code=end
