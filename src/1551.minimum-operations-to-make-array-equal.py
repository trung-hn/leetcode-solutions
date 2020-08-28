#
# @lc app=leetcode id=1551 lang=python3
#
# [1551] Minimum Operations to Make Array Equal
#

# @lc code=start
# TAGS: Math
class Solution:
    # 32 ms, 87.52. Time and Space: O(1)
    def minOperations(self, n: int) -> int:
        no = n // 2
        if n % 2:
            if no % 2: # 2 + 4 + 6 = (0 + 1 + 2 + 3)  * 2
                return (no * ((no + 1) // 2)) * 2
            else: # 2 + 4 + 6 + 8 = (1 + 2 + 3 + 4)  * 2
                return ((no + 1) * (no // 2)) * 2
        else:
            if no % 2: # 1 + 3 + 5 = (1 + 2) * 2 + 3
                return ((no) * (no // 2)) * 2 + no
            else: # 1 + 3 + 5 + 7 = (0 + 1 + 2 + 3) * 2 + 4
                return ((no - 1) * (no // 2)) * 2 + no

# @lc code=end