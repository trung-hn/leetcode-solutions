#
# @lc app=leetcode id=2673 lang=python3
#
# [2673] Make Costs of Paths Equal in a Binary Tree
#


# @lc code=start
# TAGS: Array, Dynamic Programming, Greedy, Tree, Binary Tree
class Solution:
    # Time: O(N). Space: O(logN)
    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.counter = 0

        def dfs(node=1):
            if node > len(cost):
                return 0
            left = dfs(node * 2)
            right = dfs(node * 2 + 1)
            self.counter += abs(left - right)
            return max(left, right) + cost[node - 1]

        dfs()
        return self.counter


# @lc code=end
