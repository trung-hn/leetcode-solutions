#
# @lc app=leetcode id=967 lang=python3
#
# [967] Numbers With Same Consecutive Differences
#

# @lc code=start
class Solution:
    # dfs. Time 76 ms, 14.81%. Time: O(N*2^N). Space: O(2^N)
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        self.ans = set()
        if N == 1: self.ans.add(0)
        def dfs(n, N, K, sofar=''):
            if len(sofar) == N:
                self.ans.add(sofar)
                return
            if n < 0 or n > 9: return
            dfs(n + K, N, K, sofar + str(n))
            dfs(n - K, N, K, sofar + str(n))
        
        for i in range(1, 10):
            dfs(i, N, K)
        return self.ans
# @lc code=end

