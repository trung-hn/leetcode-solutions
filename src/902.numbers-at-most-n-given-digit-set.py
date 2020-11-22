#
# @lc app=leetcode id=902 lang=python3
#
# [902] Numbers At Most N Given Digit Set
#

# @lc code=start
# TAGS: Math, Dynamic Programming
class Solution:
    # LTE. Time: O(K!)
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = [int(d) for d in digits]
        self.ans = 0
        def dfs(sofar=0):
            if sofar > n: return
            if sofar != 0:
                self.ans += 1
            for d in digits:
                dfs(sofar * 10 + d)
        dfs()
        return self.ans
    
    # TLE. Time: O(logN). Space: O(1)
    # Loop over each digit and calculate the possibilities for digits after that
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n = str(n)
        ans = 0
        for i in range(1, len(n)):
            ans += len(digits) ** i

        i = 0
        for i, c in enumerate(n, 1):
            smaller_digits = sum(d < c for d in digits)
            ans += smaller_digits * len(digits) ** (len(n) - i)
            if i == len(n) and c in digits: ans += 1
            if smaller_digits == len(digits): break
            if c not in digits: break
        return ans

# @lc code=end

