#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
# TAGS: Hash Table, Bit Manipulation
# REVIEWME: Bit Manipulation
class Solution:
    # 32 ms, 98%. Time: O(N). Space: O(1) because of alphabet
    def findTheDifference1(self, s: str, t: str) -> str:
        rv = collections.Counter(t) - collections.Counter(s)
        return "".join(rv.keys())
    
    # Bit Manipulation. Detection odd occurence. Time: O(N). Space: O(1) 
    def findTheDifference(self, s: str, t: str) -> str:
        temp = 0
        for c in s + t:
            temp ^= ord(c)
        return chr(temp)
# @lc code=end

