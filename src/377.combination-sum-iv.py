#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start
# TAGS: Dynamic Programming


class Solution:
    # 48 ms, 28.27%. Time: O(T). Space: O(T)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(sofar=0):
            if sofar > target:
                return 0
            if sofar == target:
                return 1
            return sum(dfs(sofar + n) for n in nums)
        return dfs()
# @lc code=end
