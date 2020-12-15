#
# @lc app=leetcode id=1663 lang=python3
#
# [1663] Smallest String With A Given Numeric Value
#

# @lc code=start
# TAGS: Greedy
class Solution:
    # 44 ms, Time: O(N). Space: O(1)
    def getSmallestString(self, n: int, k: int) -> str:
        Zs = k // 26
        As_need = n - Zs
        As_have = k - Zs * 26
        
        if As_need == 0: return "z" * Zs
        while As_need > As_have:
            Zs -= 1
            As_need += 1
            As_have += 26
        As_diff = As_have - As_need
        return "a" * (As_need - 1) + chr(ord("a") + As_diff)  + "z" * Zs
    
    # 32 ms, 97.70%. Cleaner solution. Time: O(N). Space: O(1)
    def getSmallestString(self, n: int, k: int) -> str:
        # Fill in "a" at all position, and then fill in z. Notice that we // 25 instead of 26
        Zs = (k - n) // 25
        if Zs == n: return "z" * Zs
        
        As = n - Zs - 1 # Leave out 1 middle character
        mid = k - (As + Zs * 26)
        return "a" * As + chr(ord("a") + mid - 1)  + "z" * Zs
# @lc code=end

