#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
# TAGS: Sort, Ordered Map
# REVIEWME: Bucket Sort. 
class Solution:
    # There is another solution that is related to Self-Balanced Tree
    # Time and Space: O(N). Bucket Sort. Copied from discussion.
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in range(n):
            m = nums[i] // w 
            
            # Numbers that are (t + 1) near each other will be in the same bucket
            # or neighbor buckets but need to make sure of the condition
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]

            # Remove those buckets that are far away.
            # It is important to note that we will not remove duplicate buckets 
            # because if duplicate buckets exist, the program already retursn Tree
            if i >= k: del d[nums[i - k] // w]
        return False
# @lc code=end

