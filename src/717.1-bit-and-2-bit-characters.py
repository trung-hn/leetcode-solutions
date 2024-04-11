#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#


# @lc code=start
# TAGS: Array, Greedy
# REVIEWME: Greedy
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ptr = 0
        while ptr < len(bits) - 1:
            ptr += 2 if bits[ptr] == 1 else 1
        return ptr == len(bits) - 1


# @lc code=end
