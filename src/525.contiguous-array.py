#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
# TAGS: Hash Table
# REVIEWME: Very good problem. Think graph
class Solution:
    """
    In both solution, Time is O(N) and Space is O(N)
    """
    # 872 ms, 95.30%
    def findMaxLength(self, nums: List[int]) -> int:
        count = max_len = 0 
        D = {0:0}
        for i, num in enumerate(nums, 1):
            count += 1 if num else -1
            if count in D:
                max_len = max(max_len, i - D[count])
            else:
                D[count] = i
        return max_len
    # 924 ms, 63.58%
    def findMaxLength(self, nums: List[int]) -> int:
        count = max_len = 0 
        D = {0:0}
        for i, num in enumerate(nums, 1):
            count += 1 if num else -1
            max_len = max(max_len, i - D.setdefault(count, i))
        return max_len
     
# @lc code=end

