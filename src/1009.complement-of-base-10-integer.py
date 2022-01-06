#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start


class Solution:
    # 32 ms, 90%
    def bitwiseComplement1(self, N: int) -> int:
        binary = bin(N)[2:]
        return int("".join(["0" if i == "1" else "1" for i in binary]), 2)

    # 36 ms
    def bitwiseComplement(self, N: int) -> int:
        # 11111 = 1 + 2 + 4 + 8 + ... iteratively, it equals 1, 3, 7, 15
        i = 1
        while i < N:
            i = i * 2 + 1
        return i - N

    def bitwiseComplement(self, N: int) -> int:
        upper = 1
        while upper < N:
            upper = upper * 2 + 1
        return upper - N
# @lc code=end
