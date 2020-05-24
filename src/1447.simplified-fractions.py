#
# @lc app=leetcode id=1447 lang=python3
#
# [1447] Simplified Fractions
#

# @lc code=start
# TAGS: Math
class Solution:
    # 260 ms, 75.31%. Using gcd
    # Time: O(N^2 * logN) beacause gcd() takes O(logN)
    # Space: O(logN) because of recursion
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a, b):
            # This is Euclidean Algorithm. Or we can just use built in gcd
            while b:
                a, b = b, a % b
            return a
        ans = []
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if math.gcd(i, j) == 1: # means they are co-prime
                    ans.append(f"{i}/{j}")
        return ans

    # Method 2: using set. 
    # Time is O(N^2) because there is no recursion. 
    # Space O(N)
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        seen = set()
        for denominator in range(2,n+1):
            for numerator in range(1,denominator):
                num = round(numerator/denominator, 15)
                if num in seen: continue
                res.append(f"{numerator}/{denominator}")
                seen.add(num)
        return res
# @lc code=end

