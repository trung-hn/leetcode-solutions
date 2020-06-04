#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    # Time: O(N), Space: O(1)
    for i in range(len(s)//2):
        s[i], s[~i] = s[~i], s[i]
        
# @lc code=end

