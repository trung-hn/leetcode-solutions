#
# @lc app=leetcode id=1726 lang=python3
#
# [1726] Tuple with Same Product
#

# @lc code=start
# TAGS: Array, Hash Table
import collections
class Solution:
    # 676 ms, 62.29%. Time: O(N^2). Space: O(N)
    def tupleSameProduct(self, nums: List[int]) -> int:
        counter = collections.Counter()
        for i in range(len(nums)):
            num1 = nums[i]
            for num2 in nums[i + 1:]:
                counter[num1 * num2] += 1
        
        total = 0
        for freq in counter.values():
            total += 2 * (freq - 1) * 2 * freq
            # or freq * (freq - 1) * 4 meaning choosing 2 out of freq and each of those have 4 variations
        return total


# @lc code=end

