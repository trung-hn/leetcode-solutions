#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
# TAGS: Math, String
class Solution:
    def romanToInt(self, s: str) -> int:
        return_val = 0
        pair={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            return_val += pair[s[i]]
            if i== 0: continue
            # Subtract the amount already added (times 2) if next number is bigger
            if pair[s[i]] > pair[s[i - 1]]:
                return_val -= pair[s[i - 1]] * 2
        return return_val

# @lc code=end

