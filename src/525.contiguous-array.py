#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#

# @lc code=start
# TAGS: Hash Table
# REVIEWME: Very good problem. Think graph
class Solution:
    # TLE. Time: O(N^3). Space: O(1)
    def findMaxLength(self, nums: List[int]) -> int:
        L = len(nums)
        if L % 2: L -= 1
        for length in range(L, 0, -2): # O(N)
            for i in range(len(nums) - length + 1): # O(N)
                ones = sum(nums[i : i + length]) # O(N)
                if ones == length // 2:
                    return length
        return 0

    # 872 ms, 95.30%. Time: O(N), Space: O(N)
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

    # 924 ms, 63.58%. Pythonic. Time: O(N), Space: O(N)
    def findMaxLength(self, nums: List[int]) -> int:
        count = max_len = 0 
        D = {0:0}
        for i, num in enumerate(nums, 1):
            count += 1 if num else -1
            max_len = max(max_len, i - D.setdefault(count, i))
        return max_len
     
     
# @lc code=end

