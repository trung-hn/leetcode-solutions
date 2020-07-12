#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
# TAGS: Backtracking, Bit Manipulation
# REVIEWME: There are other solutions with similar complexity
class Solution:
    # 36 ms, 70%. Time and Space: O(N 2^N)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def recurse(nums, sofar = []):
            ans.append(sofar)
            for i, num in enumerate(nums):
                recurse(nums[i + 1 :], sofar + [num])
        recurse(nums)
        return ans
# @lc code=end

