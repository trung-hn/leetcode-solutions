#
# @lc app=leetcode id=1502 lang=python3
#
# [1502] Can Make Arithmetic Progression From Sequence
#

# @lc code=start
# TAGS: Array
class Solution:
    # 44 ms, 78.95 %. Time O(NlogN), Space: O(1)
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for v1, v2 in zip(arr[1:], arr[2:]):
            if v2 - v1 != diff:
                return False
        return True
# @lc code=end

