#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#

# @lc code=start
# TAGS: Bit Manipulation.
class Solution:
    # Time: O(N). Space: O(1)
    def xorOperation(self, n: int, start: int) -> int:
        ans = start
        for i in range(1, n):
            ans ^= (start + 2*i)
        return ans
    
    # 32 ms, 65.3%. Time and Space: O(1) but requires to notice the pattern. 
    # More in discussion:
    # https://leetcode.com/problems/xor-operation-in-an-array/discuss/699141/VISUAL-SOLUTION-Python-or-O(1)-Time-or-O(1)-Space-or
    def xorOperation(self, n: int, start: int) -> int:
        last = start + 2 * (n-1)

        if start % 4 <= 1:
            if n % 4 == 1: 
                return last
            elif n % 4 == 2: 
                return 2
            elif n % 4 == 3: 
                return 2 ^ last
            else: 
                return 0
        else:
            if n % 4 == 1: 
                return start
            elif n % 4 == 2: 
                return start ^ last
            elif n % 4 == 3: 
                return start ^ 2
            else: 
                return start ^ 2 ^ last
# @lc code=end

