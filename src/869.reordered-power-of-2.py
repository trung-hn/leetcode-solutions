#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#

# @lc code=start
# TAGS: Math
from collections import Counter
class Solution:
    # 24 ms, 98.39%. Time: O(logN) Space: O(N)
    def reorderedPowerOf2(self, N: int) -> bool:
        order_of_2 = [2**val for val in range(32)]
        return any(Counter(str(N)) == Counter(str(val)) for val in order_of_2)
        
# @lc code=end

