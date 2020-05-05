#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
# TAG: Bit Manipulation
class Solution:
    # 28 ms, 61%. O(N)
    def findComplement(self, num: int) -> int:
        return int("".join(["1" if b == "0" else "0" for b in bin(num)[2:]]), 2)
    
    # 28 ms, 61%. Bitwise op
    def findComplement(self, num: int) -> int:
        temp = 1 << num.bit_length()
        return (temp - 1) ^ num
# @lc code=end

