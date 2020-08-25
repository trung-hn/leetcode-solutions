#
# @lc app=leetcode id=1528 lang=python3
#
# [1528] Shuffle String
#

# @lc code=start
# TAGS: String
class Solution:
    # 68 ms, 41.4%. Time and Space: O(N)
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_s = [0] * len(indices)
        for i in range(len(indices)):
            new_s[indices[i]] = s[i]
        return "".join(new_s)
# @lc code=end

