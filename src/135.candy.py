#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
# TAGS: Greeedy
# REVIEWME: Greeedy


class Solution:
    """
    There is another solution with O(1) Space.
    """
    # Time and Space: O(N). Greedy

    def candy(self, ratings: List[int]) -> int:

        candies = [1] * len(ratings)

        # forward. Only increase candy by 1 at a time.
        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1

        # backward.
        for i in reversed(range(1, len(ratings))):
            if ratings[i - 1] > ratings[i]:
                if candies[i - 1] <= candies[i]:
                    candies[i - 1] = candies[i] + 1
        return sum(candies)
# @lc code=end
