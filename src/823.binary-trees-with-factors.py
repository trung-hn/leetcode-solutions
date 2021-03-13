#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#

# @lc code=start
# TAGS: Dynamic Programming


class Solution:
    # 204 ms, 89.56%. Time: O(N^2). Space: O(N)
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        visited = {}

        def dfs(n):
            if n in visited:
                return visited[n]
            rv = 1  # tree can have 1 node.
            for n1 in arr:
                if n1 > int(n ** 0.5):
                    break
                n2, r = divmod(n, n1)
                if r != 0 or n2 not in nums:
                    continue
                prod = dfs(n1) * dfs(n2)
                rv += prod if n1 == n2 else prod * 2
            visited[n] = rv
            return visited[n] % MOD

        nums = set(arr)
        arr.sort()
        total = sum(dfs(n) % MOD for n in arr)
        return total % MOD
# @lc code=end
