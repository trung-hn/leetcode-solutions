#
# @lc app=leetcode id=1525 lang=python3
#
# [1525] Number of Good Ways to Split a String
#

# @lc code=start
# TAGS: String
class Solution:
    # 168 ms, 88.72 %. Time and Space: O(N)
    def numSplits(self, s: str) -> int:
        left = [0] * len(s)
        right = [0] * len(s)

        set1 = set()
        set2 = set()
        
        for i in range(len(s)):
            set1.add(s[i])
            left[i] = len(set1)
        
            set2.add(s[~i])
            right[~i] = len(set2)
        return sum(l == r for l, r in zip(left, right[1:]))

# @lc code=end

