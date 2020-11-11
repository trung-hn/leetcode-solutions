#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#

# @lc code=start
# TAGS: Math
class Solution:
    # Time and Space: O(1)
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if len(set(tuple(p) for p in (p1,p2,p3,p4))) < 4: return False
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        def is_perpendicular(p1, p2, p3, p4):
            # check if p1-p2 is perpendicular wiht p3-p4
            return (p1[1] - p2[1]) * (p3[1] - p4[1]) == - (p3[0] - p4[0]) * (p1[0] - p2[0])
        cond1 = is_perpendicular(p1, p2, p1, p3)
        cond2 = is_perpendicular(p2, p1, p2, p4)
        cond3 = is_perpendicular(p3, p1, p3, p4)
        cond4 = is_perpendicular(p1, p4, p2, p3)
        return cond1 and cond2 and cond3 and cond4

    # get all length of lines in the shape: square can only have 2 different length of lines
    # We use complex number just to make it cleaner to right function
    def validSquare(self, *points):
        points = (complex(x, y) for x, y in  points)
        distance = lambda p: abs(p[0] - p[1])
        dists = map(distance, combinations(points, 2))
        return set(Counter(dists).values()) == {4, 2}
# @lc code=end

