#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
# TAGS: Array, Hash Table
class Solution:
    # 344 ms, 10.61%. Using the property of modulo. Time: O(N). Space: O(K). 2 passes
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        presum = [0]
        for val in A:
            presum.append(presum[-1] + val)
        ans = 0
        visited = collections.Counter()
        for val in presum:
            ans += visited[val % K]
            visited[val % K] += 1
        return ans
    
    # 288 ms, Time: O(N). Space: O(K)
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        visited = [1] + [0] * K
        prefix = ans = 0
        for val in A:
            prefix += val
            ans += visited[prefix % K]
            visited[prefix % K] += 1
        return ans
            
# @lc code=end

