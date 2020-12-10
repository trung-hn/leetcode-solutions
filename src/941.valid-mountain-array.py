#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#

# @lc code=start
# TAGS: Array
class Solution:
    # 188 ms, 93.89%. Time: O(N). Space: O(1)
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) == 1: return False
        if arr[0] >= arr[1] or arr[-1] >= arr[-2]: return False
        up = True
        for v1, v2 in zip(arr, arr[1:]):
            if up and v1 > v2:
                up = False
            elif not up and v1 <= v2:
                return False
        return True
# @lc code=end

