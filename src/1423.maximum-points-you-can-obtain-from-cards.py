#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
# TAGS: Array, Dynamic Programming, Sliding Window
# REVIEWME: Array, Sliding Window


class Solution:
    """
    At first, i thought this is a DP problem and try dfs (with memo). Input is too large.

    Approach:
    left contains scenario when we pick cards from left
    right contains scenario when we pick cards from right

    return max of sum of both

    Reduce Space to O(1) by pre calculating "right" and calculate "left" on the fly

    Another way to do this: Sliding window the middle values.
    """

    # 428 ms, 42.12%. Time and Space: O(K).

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = [0] * (k + 1)
        right = [0] * (k + 1)
        for i in range(k):
            left[i + 1] = left[i] + cardPoints[i]
            right[~i - 1] = right[~i] + cardPoints[~i]
        return max(l + r for l, r in zip(left, right))

    # 408 ms, 77.93%. Time: O(K). Space: O(1)

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        right = sum(cardPoints[-k:])
        result = left + right
        for i in range(k):
            left += cardPoints[i]
            right -= cardPoints[-k + i]
            result = max(result, left + right)
        return result
# @lc code=end
