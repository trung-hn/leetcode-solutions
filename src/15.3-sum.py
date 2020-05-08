#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    # 1604 ms.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rv = set()
        nums.sort()
        target = 0
        for i, a in enumerate(nums):
            new_target = target - a
            seen = set()
            for b in nums[i + 1:]:
                if new_target - b in seen:
                    rv.add((a,new_target - b, b))
                seen.add(b)
        return rv
    # 660 ms, 94.66%. Time: O(N), Space: O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rv = []
        nums.sort()
        for i, num in enumerate(nums[:-2]):
            if num > 0: break
            if i > 0 and num == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = num + nums[l] + nums[r]
                if total < 0: l += 1
                elif total > 0: r -= 1
                else:
                    rv.append([num, nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]: l += 1
                    while l < r and nums[r] == nums[r - 1]: r -= 1
                    l += 1
                    r -= 1
        return rv    
# @lc code=end

