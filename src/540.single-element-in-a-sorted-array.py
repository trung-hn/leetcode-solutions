#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
# TAGS: Binary Search

import collections


class Solution:

    # Time and Space: O(N)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        visited = {}
        for num in nums:
            if num in visited:
                visited[num] += 1
            else:
                visited[num] = 1

        for k, v in visited.items():
            if v == 1:
                return k

    def singleNonDuplicate(self, nums: List[int]) -> int:
        visited = collections.defaultdict(int)
        for num in nums:
            visited[num] += 1

        for k, v in visited.items():
            if v == 1:
                return k

    def singleNonDuplicate(self, nums: List[int]) -> int:
        visited = set()
        for num in nums:
            if num not in visited:
                visited.add(num)
            else:
                visited.discard(num)

        return visited.pop()

    # Time: O(N). Space: O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        val = nums[0]
        for num in nums[1:]:
            val ^= num
        return val

    # 80 ms, 22.6 %. Time: O(log N). Space: O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) // 2
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[2 * mid] == nums[2 * mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo*2]
# @lc code=end
