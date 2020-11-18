#
# @lc app=leetcode id=1646 lang=python3
#
# [1646] Get Maximum in Generated Array
#

# @lc code=start
# TAGS: Array
class Solution:
    # 28 ms, 86.65%. Time and Space: O(N)
    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1: return n
        nums = [0, 1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                nums.append(nums[i // 2])
            else:
                nums.append(nums[i // 2] + nums[i // 2 + 1])
        return max(nums)
        
# @lc code=end

