#
# @lc app=leetcode id=2517 lang=python3
#
# [2517] Maximum Tastiness of Candy Basket
#

# @lc code=start
# TAGS: Array, Binary Search, Sorting
# REVIEWME: Binary Search
class Solution:
    # Time: O(NlogN). Space: O(1)
    def maximumTastiness(self, price: List[int], k: int) -> int:
        if k == 2:
            return max(price) - min(price)
        if len(set(price)) <= k:
            return 0

        def is_possible(t, k):
            """Check if it is possible to attain `t` tastiness from k candies"""
            cnt = 1
            prev = price[0]
            for p in price[1:]:
                if p - prev >= t:
                    cnt += 1
                    prev = p
            return cnt >= k
        
        price.sort()
        lo = 0
        hi = (max(price) - min(price)) // (k - 2) # minor optimization because we know highest possible tastiness.
        while lo < hi:
            mid = (lo + hi) // 2
            if is_possible(mid, k):
                lo = mid + 1
            else:
                hi = mid
        
        # Edge case: hi = mid but didn't get check. 
        return hi if is_possible(hi, k) else hi - 1



# @lc code=end

