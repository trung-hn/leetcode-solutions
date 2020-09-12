#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
# TAGS: Array, Backtracking
class Solution:
    # 36 ms, 43.98 %. Time: O(N^2). Space: O(N^2)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def dfs(sofar=[], sum_sofar=0):
            if len(sofar) > k or sum_sofar > n: return
            if len(sofar) == k and sum_sofar == n: 
                ans.append(sofar)
                return

            start = sofar[-1] if sofar else 0
            for num in range(start + 1, 10):
                dfs(sofar + [num], sum_sofar + num)
        dfs()
        return ans

# @lc code=end

