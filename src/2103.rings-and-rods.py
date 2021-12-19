#
# @lc app=leetcode id=2103 lang=python3
#
# [2103] Rings and Rods
#

# @lc code=start
# TAGS: Hash Table, String
class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            c = rings[i]
            r = int(rings[i + 1])
            rods[r].add(c)
        return sum(len(rod) == 3 for rod in rods)

# @lc code=end
