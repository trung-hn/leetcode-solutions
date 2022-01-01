#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
# TAGS: Array, Dynamic Programming
# REVIEWME: Dynamic Programming
class Solution:
    """
    Approach:
    dp[left][right] is the best (max) coins obtained by popping all balloons between left and right (non including 2 ends)
    Thus, we return dp[0][N - 1] at the end

    How to calculate dp[left][right] ?
    for each mid between left and right:
        dp[left][right] = max(itself, dp[left][mid] + dp[mid][right] + pop balloon at mid)

    In other words, this means, for each `mid` balloon between left and right, we assume there is only `mid` left over, and we pop that `mid`
    For example:
        dp[0][4] = max(
                pop balloon at i = 1,
                pop balloon at i = 2,
                pop balloon at i = 3,
                )
    `pop balloon at i = 1` need dp[0][1] and dp[1][4]

    You can see that dp at higher range 0 -> 4 requires dp at lower range 1 -> 4. 
    Thus, we need an extra loop at the top level to go through all difference levels
    """
    # 8436 ms, 61.51%. Time: O(N^3). Space: O(N^2)

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [val for val in nums if val] + [1]
        N = len(nums)
        dp = [[0] * N for _ in range(N)]

        for diff in range(2, N):
            for left in range(N - diff):
                right = left + diff
                for mid in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], dp[left][mid] + dp[mid][right]
                                          + nums[left] * nums[mid] * nums[right])

        return dp[0][-1]


# @lc code=end
