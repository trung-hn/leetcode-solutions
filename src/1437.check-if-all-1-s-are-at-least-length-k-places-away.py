#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#

# @lc code=start
# TAGS: Array
class Solution:
    # 564 ms, 66.96%. Time: O(N). Space: O(1)
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = ~k
        for i, num in enumerate(nums):
            if num == 1 and i - prev < k + 1:
                return False
            if num == 1: prev = i
        return True

    # 564 ms, 66.96%. Time: O(N). Space: O(1)
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cnt = k
        for num in nums:
            if num == 1:
                if cnt < k: return False
                cnt = 0
            else:
                cnt += 1
        return True
        
# @lc code=end

