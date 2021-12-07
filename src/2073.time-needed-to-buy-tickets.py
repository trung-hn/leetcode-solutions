#
# @lc app=leetcode id=2073 lang=python3
#
# [2073] Time Needed to Buy Tickets
#

# @lc code=start
# TAGS: Array, Queue, Simulation
class Solution:
    # 32 ms, 85.71%. Time: O(N). Space: O(1)
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0
        for i, val in enumerate(tickets):
            cnt += min(tickets[k] - bool(k < i), val)
        return cnt
# @lc code=end
