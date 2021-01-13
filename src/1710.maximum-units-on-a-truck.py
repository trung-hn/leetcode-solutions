#
# @lc app=leetcode id=1710 lang=python3
#
# [1710] Maximum Units on a Truck
#

# @lc code=start
# TAGS: Sort, Greedy
class Solution:
    # 144 ms, 98.10%. Time: O(NlogN). Space: O(N)
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[-1])
        total_unit = 0
        while boxTypes and truckSize:
            boxes, units_per = boxTypes.pop()
            new_box = min(truckSize, boxes)
            truckSize -= new_box
            total_unit += new_box * units_per
        return total_unit
            
# @lc code=end

