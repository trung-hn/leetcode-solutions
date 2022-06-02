#
# @lc app=leetcode id=2165 lang=python3
#
# [2165] Smallest Value of the Rearranged Number
#

# @lc code=start
# TAGS: Math, Sorting
import collections


class Solution:
    # Time and Space: O(logN)
    def smallestNumber(self, num: int) -> int:
        digits = collections.Counter(str(abs(num)))
        if num < 0:
            return -int("".join(d * digits[d] for d in "9876543210"))

        first = ""
        for d in "123456789":
            if digits[d]:
                digits[d] -= 1
                first = d
                break

        return int(first + "".join(d * digits[d] for d in "0123456789"))


# @lc code=end
