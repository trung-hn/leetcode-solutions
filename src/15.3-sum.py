#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
# TAGS: Array, Two Pointers


class Solution:
    # 724 ms, 86.78%. Time and Space: O(N^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i, first in enumerate(nums):

            # Skip obvious cases
            if first > 0:
                break
            if i and first == nums[i-1]:
                continue

            # Essentially 2 sum problem
            seen = {}
            for second in nums[i + 1:]:
                if second in seen:
                    ans.add(seen[second] + (second,))
                seen[- first - second] = (first, second)
        return ans

    # 660 ms, 94.66%. Time: O(N^2), Space: O(N^2)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rv = []
        nums.sort()
        for i, num in enumerate(nums[:-2]):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    rv.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return rv
# @lc code=end
