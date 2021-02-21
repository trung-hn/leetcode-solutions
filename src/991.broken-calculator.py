#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#

# @lc code=start
# TAGS: Math, Greedy
class Solution:
    # 20 ms, 99%. Time: O(logN). Space: O(1). 
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y: return X - Y
        
        cnt = 0
        while X < Y:
            X *= 2
            cnt += 1
            
        diff = X - Y
        for i in range(cnt, -1, -1):
            d, diff = divmod(diff, 2**i)
            cnt += d
        return cnt
            
                
        
# @lc code=end

