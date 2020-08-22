#
# @lc app=leetcode id=497 lang=python3
#
# [497] Random Point in Non-overlapping Rectangles
#

# @lc code=start
# TAGS: Design, Binary Search
import random
import bisect
class Solution:
    """
    Approach: Create a pool of rect_choices with choices propotion to the area of rectangles
    Next, a random rectangle is chosen from this pool using Binary Search. 
    Finally, a random point is picked from this rectangle 
    """
    # 212 ms,  70.52%. Time: O(log(|rect|)). Space: O(|rects|)
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.rect_choices = []
        area = 0
        for x1, y1, x2, y2 in rects:
            area += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.rect_choices.append(area)


    def pick(self) -> List[int]:
        rect_choice = random.choice(range(1, self.rect_choices[-1] + 1))
        rect_index = bisect.bisect_left(self.rect_choices, rect_choice)
        x1, y1, x2, y2 = self.rects[rect_index]
        return (random.randint(x1, x2), random.randint(y1, y2))

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
# @lc code=end

