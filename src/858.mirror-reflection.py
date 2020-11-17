#
# @lc app=leetcode id=858 lang=python3
#
# [858] Mirror Reflection
#

# @lc code=start
# TAGS: Math
# REVIEWME: Math
import fractions
class Solution:
    # 24 ms, 91.58%. Time: O(logN). Space: O(1)
    def mirrorReflection(self, p: int, q: int) -> int:
        if q == 0: return 0
        val = 0
        while val == 0 or val % p:
            val += q
            
        if (val // p) % 2 == 0: return 0
        if (val // q) % 2 : return 1
        return 2
    
    # 24 ms, 91.58%. using fraction. Simplified version of above.
    def mirrorReflection(self, p: int, q: int) -> int:
        num = fractions.Fraction(q, p)
        val = num.numerator * num.denominator
        if (val // num.denominator) % 2 == 0: return 0
        if (val // num.numerator) % 2 : return 1
        return 2
    
    # 24 ms, 91.58%. Use gcd. Simplified version of above.
    def mirrorReflection(self, p: int, q: int) -> int:
        gcd = math.gcd(p, q)
        p //= gcd
        q //= gcd
        if q % 2 == 0: return 0
        if p % 2 : return 1
        return 2
# @lc code=end

