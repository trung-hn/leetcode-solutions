#
# @lc app=leetcode id=1624 lang=python3
#
# [1624] Largest Substring Between Two Equal Characters
#

# @lc code=start
# TAGS: String
class Solution:
    # 16 ms, 100%. Time: O(N). Space: O(1)
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        indices = {}
        for i, c in enumerate(s):
            if c not in indices:
                indices[c] = [i, i]
            indices[c][1] = i
            ans = max(ans,  indices[c][1] - indices[c][0] - 1)
        return ans
# @lc code=end

