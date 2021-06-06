#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
# TAGS: Array


class Solution:
    # 420 ms, 22.54%. O(NlogN). Space: O(N)
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(set(nums))
        ans = cnt = 1
        for n1, n2 in zip(nums, nums[1:]):
            if n1 + 1 == n2:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        return ans

    # 232 ms, 29.05%. Time and Space: O(N)
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            # Number is not start of a sequence
            if num - 1 in nums:
                continue
            cnt = 1

            # Only when number is the start of a sequence.
            while num + 1 in nums:
                num += 1
                cnt += 1
            ans = max(ans, cnt)
        return ans
# @lc code=end
