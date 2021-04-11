#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#

# @lc code=start
# TAGS: DFS


class Solution:
    """
    Approach: Typical Combination problems.
    Recursively iterate through all numbers and add to visited
    """

    # 236 ms, 50.00%. Time and Space: O(Combination)
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def dfs(start=0, seq=[]):
            if len(seq) > 1:
                self.visited.add(tuple(seq))
            if start == len(nums):
                return

            for i in range(start + 1, len(nums)):
                if seq[-1] <= nums[i]:
                    dfs(i, seq + [nums[i]])

        N = len(nums)
        self.visited = set()
        for i, num in enumerate(nums):
            dfs(i, [num])
        return self.visited
# @lc code=end
