#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
# TAGS: Math, Pythonic, Geometry
# REVIEWME:
class Solution:
    # 60 ms, 77.13%. Check slope. First solution, not clean. 
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = None
        for (x1, y1) , (x2, y2) in zip(coordinates, coordinates[1:]):
            if x1 == x2:
                sl = float('inf')
            else:
                sl = (y2 - y1) / (x2 - x1)
            if slope is None:
                slope = sl
            else:
                if slope != sl:
                    return False
        return True
    # 60 ms, 77.13%
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        slope = None
        for (x1, y1) , (x2, y2), (x3, y3) in zip(coordinates, coordinates[1:], coordinates[2:]):
            if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
                return False
        return True
    # 68 ms, 20.60%. From discussion. 
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)        
# @lc code=end

