#
# @lc app=leetcode id=1509 lang=python3
#
# [1509] Minimum Difference Between Largest and Smallest Value in Three Moves
#

# @lc code=start
# TAGS: Greedy
class Solution:
    # 460 ms, 60.87%. Time: O(NlogN). Space: O(1)
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4: return 0
        nums.sort()
        pick_last3 = nums[-4] - nums[0]
        pick_first3 = nums[-1] - nums[3]
        pick_last2_first1 = nums[-3] - nums[1]
        pick_last1_first2 = nums[-2] - nums[2]
        return min(pick_last3, pick_first3, pick_last1_first2, pick_last2_first1)

    # 448 ms, 63.62%. Generalize so it will work for all k
    def minDifference(self, nums: List[int]) -> int:
        k = 3
        if len(nums) <= k + 1: return 0
        nums.sort()

        rv = float("inf")
        for i in range(k + 1):
            rv = min(rv, nums[~k + i] - nums[i])
        return rv
        
# @lc code=end
