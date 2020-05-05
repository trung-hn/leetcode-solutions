#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    def firstUniqChar(self, s: str) -> int:
        d=collections.Counter(s)
        
        for i in range(len(s)):
            if d[s[i]]==1: return i
        return -1
# @lc code=end

