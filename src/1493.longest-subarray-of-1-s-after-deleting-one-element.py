#
# @lc app=leetcode id=1493 lang=python3
#
# [1493] Longest Subarray of 1's After Deleting One Element
#

# @lc code=start
# TAGS: Array
class Solution:
    # 38.82%. Time: O(N), Space: O(1)
    def longestSubarray(self, nums: List[int]) -> int:
        cnt1 = ans = 0
        cnt2 = -1 # Need this because we must delete 1 character. 
        for n in nums:
            if n:
                cnt1 += 1
            else:
                cnt2 = cnt1
                cnt1 = 0
            ans = max(ans, cnt1 + cnt2)
        return ans
            
        
# @lc code=end

