#
# @lc app=leetcode id=1861 lang=python3
#
# [1861] Rotating the Box
#

# @lc code=start
# TAGS: Array, Two Pointers


class Solution:
    """
    Approach: Go row by row
    from the end of the row, simulate gravity
    return the rotated version of box. 
    """
    # 3536 ms, 42.25%. Time: O(R*C). Space: O(1)

    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        C = len(box[0])
        for row in box:
            empty_ptr = C - 1
            for c in reversed(range(C)):

                # Move empty pointer if we see obstacle
                if row[c] == "*":
                    empty_ptr = c - 1

                # Switch places and move empty_ptr
                # empty_ptr can be == c
                elif row[c] == "#":
                    row[empty_ptr], row[c] = row[c], row[empty_ptr]
                    empty_ptr -= 1

        # rotate right 90 degree.
        return zip(*reversed(box))

# @lc code=end
