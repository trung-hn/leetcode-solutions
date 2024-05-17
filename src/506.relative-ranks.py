#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#


# @lc code=start
# TAGS: Array, Sorting, Heap (Priority Queue)
class Solution:
    # 60 ms, 98%. O(NlogN) because of sort
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        rank = {}
        for i, num in enumerate(sorted(nums, reverse=True)):
            if i == 0:
                rank[num] = "Gold Medal"
            elif i == 1:
                rank[num] = "Silver Medal"
            elif i == 2:
                rank[num] = "Bronze Medal"
            else:
                rank[num] = str(i + 1)
        return [rank[num] for num in nums]


# @lc code=end
