#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
# TAGS: Dynamic Programming, String
class Solution:
    # 276 ms, 74.96%. Time: O(N^2). Space: O(N) assuming words have the same length
    def minDistance(self, word1: str, word2: str) -> int:
        prev = list(range(len(word1) + 1))
        for c2 in word2:
            cur = [prev[0] + 1]
            for i in range(len(word1)):
                if c2 != word1[i]: prev[i] += 2 
                cur.append(min(prev[i], cur[-1] + 1, prev[i + 1] + 1))
            prev = cur
        return prev[-1]  
# @lc code=end

