#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#

# @lc code=start
# TAGS: Greedy, Sort
# REVIEWME: Greedy
class Solution:
    # 424 ms, 825 %. Time: O(NlogN). Space: O(1) if not consider internal memory. 
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        ------   
         ---    <- make this the new end.
          -----
           ^
           |
         shoot
                  -----
                    --------
                       ---------
        """
        if not points: return 0        
        
        points.sort()
        arrows = pop_ptr = overlap_ptr = 0
        while overlap_ptr < len(points):
            if points[overlap_ptr][0] > points[pop_ptr][-1]:
                pop_ptr = overlap_ptr
                arrows += 1
            points[pop_ptr][-1] = min(points[pop_ptr][-1], points[overlap_ptr][-1])
            overlap_ptr += 1
        return arrows + 1

    # 392 ms, 98.46%. From the article. It is also Greedy but from a different perspective.
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        ------
                 ---
            ---------
                ------
            -----------
                     ---
        """
        if not points: return 0
        
        points.sort(key = lambda x : x[1])
        arrows = 0
        pop_end = points[0][-1]
        for start, end in points:
            if start > pop_end:
                arrows += 1
                pop_end = end

        return arrows + 1
# @lc code=end

