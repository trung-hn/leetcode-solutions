#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
# TAGS: LRU Cache, Dynamic Programming.
from functools import lru_cache

class Solution:
    """
    More: https://leetcode.com/problems/minimum-cost-for-tickets/discuss/226659/Two-DP-solutions-with-pictures
    """
    # 84 ms, 14.16 %. Time and Space: O(365)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day_set = set(days)

        @lru_cache(None) # This is memoization because dfs(day + d) is called a lot. Use this instead of creating a memoization ourselves. 
        def dfs(day):
            if day > 365:
                return 0
            elif day in day_set:
                return min(dfs(day + d) + c for d, c in zip([1, 7, 30], costs))
            else:
                return dfs(day + 1)
        return dfs(1)

# @lc code=end

