#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start
# TAGS: Two Pointers.
class Solution:
    # 1216 ms, 91.76%. Time: O(N). Space: O(1)
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited = set()
        total = ans = ptr = 0
        for num in nums:
            while num in visited:
                total -= nums[ptr]
                visited.discard(nums[ptr])
                ptr += 1
            total += num
            visited.add(num)
            ans = max(ans, total)
        return ans

# @lc code=end
