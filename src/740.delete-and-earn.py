#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
# TAGS: Dynamic Programming


class Solution:
    # 48 ms, 94.60%. Time and Space: O(N)
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = [0] * (max(nums) + 1)
        for num, freq in collections.Counter(nums).items():
            counter[num] = num * freq

        # Similar to robbing house problem
        skip = take = 0
        for point in counter:
            new_take = skip + point  # rob this house
            new_skip = max(skip, take)  # skip this house
            skip = new_skip
            take = new_take
        return max(take, skip)
# @lc code=end
