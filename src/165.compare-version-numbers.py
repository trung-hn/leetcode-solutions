#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
# TAGS: String

class Solution:
    # 32 ms, 58.83 %. Time: O(N). Space: O(1)
    def compareVersion(self, version1: str, version2: str) -> int:
        for d1, d2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue="0"):
            if int(d1) > int(d2):
                return 1
            elif int(d1) < int(d2):
                return -1
        return 0
# @lc code=end

