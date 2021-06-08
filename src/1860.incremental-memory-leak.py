#
# @lc app=leetcode id=1860 lang=python3
#
# [1860] Incremental Memory Leak
#

# @lc code=start
# TAGS: Math


class Solution:
    """
    There is a Math solution with O(1) time complexity
    """
    # 296 ms, 80.05%. Brute Force. Time: O(logN). Space: O(1)

    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 0
        while 1:
            i += 1
            if memory1 >= memory2 and memory1 >= i:
                memory1 -= i
            elif memory2 >= memory1 and memory2 >= i:
                memory2 -= i
            else:
                return i, memory1, memory2

# @lc code=end
