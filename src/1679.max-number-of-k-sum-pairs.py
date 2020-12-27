#
# @lc app=leetcode id=1679 lang=python3
#
# [1679] Max Number of K-Sum Pairs
#

# @lc code=start
# TAGS: Hash Table
class Solution:
    # 632 ms, 95.03%. Time and Space: O(N)
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        ans = 0
        for val, freq in counter.items():
            key = k - val
            if key in counter:
                ans += min(freq, counter[key])
        return ans // 2 # this will deal with duplicates and when key == val
                
# @lc code=end

