#
# @lc app=leetcode id=1015 lang=python3
#
# [1015] Smallest Integer Divisible by K
#

# @lc code=start
# TAGS: Math
# REVIEWME: Math
class Solution:
    # 48 ms, 76.4%. Time: O(K). Space: O(K)
    def smallestRepunitDivByK(self, K: int) -> int:
        visited = set()
        cnt = rem = 0
        while 1:
            cnt += 1
            rem = (rem * 10 + 1) % K
            if rem in visited: return -1
            visited.add(rem)
            if rem == 0: return cnt            
            
# @lc code=end

