#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#

# @lc code=start
import collections
class Solution:
    # 32 ms, 84.24%. Time and Space: O(N)
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = collections.defaultdict(int)
        cnt = 0
        for num in nums:
            cnt += freq[num]
            freq[num] += 1
        return cnt

    # Similar solution but cleaner. 
    def numIdenticalPairs(self, A):
        return sum(k * (k - 1) / 2 for k in collections.Counter(A).values())
        
# @lc code=end

