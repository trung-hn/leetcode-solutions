#
# @lc app=leetcode id=1460 lang=python3
#
# [1460] Make Two Arrays Equal by Reversing Sub-arrays
#

# @lc code=start
class Solution:
    # 76 ms, 95.63%. O(N)
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(target) == collections.Counter(arr)
# @lc code=end

