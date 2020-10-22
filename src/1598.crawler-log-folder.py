#
# @lc app=leetcode id=1598 lang=python3
#
# [1598] Crawler Log Folder
#

# @lc code=start
class Solution:
    # 40 ms, 94.64  %. Time: O(N). Space: O(1)
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                if depth: depth -= 1
            elif log != "./":
                depth += 1
        return depth
            
# @lc code=end

