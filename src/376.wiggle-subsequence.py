#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
# TAGS: Greedy, Dynamic Programming


class Solution:
    # 32 ms, 83.94 %. Time: O(N). Space: O(1)
    def wiggleMaxLength(self, nums: List[int]) -> int:
        total = 1
        prev = None
        for n1, n2 in zip(nums, nums[1:]):
            if n1 == n2:
                continue
            cur = n1 < n2
            total += (prev != cur)
            prev = cur
        return total
# @lc code=end
