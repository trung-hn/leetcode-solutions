#
# @lc app=leetcode id=2498 lang=python3
#
# [2498] Frog Jump II
#


# @lc code=start
# TAGS: Array, Binary Search, Greedy
# REVIEWME: Greedy
class Solution:
    # 540 ms, 72.34%
    # Time: O(N). Space: O(1)
    def maxJump(self, stones: List[int]) -> int:
        """
        To get to this greedy solution, it is critical to realize the followings:
        It is optimal to step on either odd stones or even stones only (for both forward and backward)
        Thus, we just need to find the max distance between odds and evens (including the stones at the 2 ends)
        """
        # Edge case
        if len(stones) == 2:
            return stones[-1]

        ans = 0
        # Odd Path
        for i in range(3, len(stones), 2):
            ans = max(ans, stones[i] - stones[i - 2])
        # Even Path
        for i in range(2, len(stones), 2):
            ans = max(ans, stones[i] - stones[i - 2])
        return ans


# @lc code=end
