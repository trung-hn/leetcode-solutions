#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
# TAGS: Binary Search
from typing import List


class Solution:
    # 540 ms, 59.53%. Time: O(NlogM). Space: O(1). N is len(nums), M is max(nums)
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if len(piles) == H:
            return max(piles)

        def can_finish(K, H):
            total = 0
            for pile in piles:
                total += pile // K + bool(pile % K)
            return total <= H

        lo, hi = 1, max(piles)
        # Alternatively, we can init lo and hi as follows (4 times faster)
        # total = sum(piles)
        # lo, hi = math.ceil(total / H) , math.ceil(total / (H-len(piles)+1))

        while lo < hi:
            mid = (lo + hi) // 2
            if can_finish(mid, H):
                hi = mid
            else:
                lo = mid + 1
        return lo


# @lc code=end
