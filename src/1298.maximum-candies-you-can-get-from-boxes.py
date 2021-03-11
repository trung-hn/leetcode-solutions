#
# @lc app=leetcode id=1298 lang=python3
#
# [1298] Maximum Candies You Can Get from Boxes
#

# @lc code=start
# TAGS: BFS


class Solution:
    # 756 ms, 96.39%. Time: O(B+K). Space: O(B)
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        visited_boxes = set()
        total = 0
        q = initialBoxes
        for box in q:
            total += candies[box]
            for b in containedBoxes[box]:
                if status[b]:
                    q.append(b)
                visited_boxes.add(b)

            for k in keys[box]:
                if status[k] == 0 and k in visited_boxes:
                    q.append(k)
                status[k] = 1

        return total
# @lc code=end
