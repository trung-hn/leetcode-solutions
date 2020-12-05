#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#

# @lc code=start
# TAGS: Dynamic Programming
# REVIEWME: Dynamic Programming
import collections
class Solution:
    # 2844 ms, 82.28%. Time: O(K*M*N). Space: O(K*M*N)
    # Space complexity can be improved with bottom up dp (rolling array)
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        visited = {}
        def dfs(i=0, zeroes=0, ones=0, cnt=0):
            # Memoization
            if (i, zeroes, ones) in visited and visited[(i, zeroes, ones)] >= cnt: 
                return 0
            visited[(i, zeroes, ones)] = cnt
            
            if zeroes > m or ones > n: return cnt - 1
            if i == len(strs): return cnt
            take = dfs(i + 1, zeroes + freqs[i][0], ones + freqs[i][1], cnt + 1)
            skip = dfs(i + 1, zeroes, ones, cnt)
            return max(take, skip)

        freqs = [collections.Counter(s) for s in strs]
        freqs = [(c["0"], c["1"])for c in freqs]
        return dfs()
# @lc code=end

