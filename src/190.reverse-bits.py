#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
# TAGS: Bit Manipulation.
class Solution:
    """
    There are more solutions with same time complexity. Look at Article for more info
    """
    # Using String. not ideal solution
    def reverseBits(self, n: int) -> int:
        s=[x for x in "{:032b}".format(n)]
        for i in range(len(s)//2):
            s[i], s[~i]=s[~i], s[i]
        return int("".join(s), 2)
    
    # 32 ms, 48%
    def reverseBits(self, n: int) -> int:
        def masked_me(n, index):
            return n & (1 << index) > 0
        rv = 0
        for i in range(32):
            if masked_me(n, 31 - i): rv += 2**i
        return rv
            
# @lc code=end

