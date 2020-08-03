#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    # Time and Space: O(N)
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1: return True
        
        modified_s="".join([c.lower() for c in s if c.isalnum()])
        print()
        return modified_s==modified_s[::-1]
    
    # Time: O(N). Space: O(1)
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

# @lc code=end

