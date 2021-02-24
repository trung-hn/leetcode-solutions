#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
# TAGS: Array, Binary Search
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def within_D_days(cap, D):
            days = 1
            cur = 0
            for w in weights:
                if cur + w > cap:
                    days += 1
                    cur = 0
                cur += w
            return days <= D
        
        lo = max(weights)
        hi = sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if within_D_days(mid, D):
                hi = mid
            else:
                lo = mid + 1
        return lo
# @lc code=end

