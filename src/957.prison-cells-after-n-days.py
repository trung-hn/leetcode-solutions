#
# @lc app=leetcode id=957 lang=python3
#
# [957] Prison Cells After N Days
#

# @lc code=start
# TAGS: Hash Table
class Solution:
    """
    Tricky problem. You need to find the pattern:
    The cycle repeat itself after 14 iterations.
    A General approach of this would be to use hashmap to find determine visited array and next array in chain
    More here: https://leetcode.com/problems/prison-cells-after-n-days/discuss/205684/JavaPython-Find-the-Loop-or-Mod-14
    """
    # 52 ms, 21.21%. Time: O(1), Space: O(1)
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        N = N % 14
        if N == 0: N += 14 # due to numbers that are multiple of 14 (Think about number at index 0 and 7)
        prev = cells
        curr = [0] * 8
        for _ in range(N):
            for i in range(1, 7):
                val = not (prev[i - 1] ^ prev[i + 1])
                curr[i] = 1 if val else 0 
            prev = curr[:]
        return prev

# @lc code=end

# [0,1,1,0,0,0,0,0] 0
# [0,0,0,0,1,1,1,0] 1
# [0,1,1,0,0,1,0,0] 2
# [0,0,0,0,0,1,0,0] 3
# [0,1,1,1,0,1,0,0] 4
# [0,0,1,0,1,1,0,0] 5
# [0,0,1,1,0,0,0,0] 6
# [0,0,0,0,0,1,1,0] 7
# [0,1,1,1,0,0,0,0] 8
# [0,0,1,0,0,1,1,0] 9
# [0,0,1,0,0,0,0,0] 10 
# [0,0,1,0,1,1,1,0] 11
# [0,0,1,1,0,1,0,0] 12
# [0,0,0,0,1,1,0,0] 13
# [0,1,1,0,0,0,0,0] 14
# [0,0,0,0,1,1,1,0] 15
# [0,1,1,0,0,1,0,0] 16
# [0,0,0,0,0,1,0,0] 17
# [0,1,1,1,0,1,0,0] 18
# [0,0,1,0,1,1,0,0] 19