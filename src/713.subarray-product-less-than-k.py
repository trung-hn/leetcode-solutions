#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#

# @lc code=start
# TAGS: Array, Two Pointers
# REVIEWME: Two Pointers.
class Solution:
    # 1156 ms, 81.15%. Time: O(N). Space: O(1). Sliding Window
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        total = 1
        cnt = i = j = 0
        while i < len(nums):
            total *= nums[i]
            if total >= k:
                while j < i and total >= k:
                    total /= nums[j]
                    j += 1
            if nums[i] < k:
                cnt += (i - j + 1)
            i += 1
        return cnt
# @lc code=end

