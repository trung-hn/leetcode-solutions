#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#

# @lc code=start
# TAGS: Array


class Solution:
    # 1416 ms. Time: O(N^2) Space: O(N)
    def numTeams(self, ratings: List[int]) -> int:
        cnt = [[0] * 2 for _ in range(len(ratings))]
        for i in range(len(ratings)):
            for j in range(i + 1, len(ratings)):
                if ratings[i] > ratings[j]:
                    cnt[i][0] += 1  # amt lt val at i
                else:
                    cnt[i][1] += 1  # amt gt val at i

        total = 0
        for i in range(len(ratings)):
            for j in range(i + 1, len(ratings)):
                if ratings[i] > ratings[j]:
                    # check how many c lt b
                    total += cnt[j][0]
                else:
                    # check how many c gt b
                    total += cnt[j][1]
        return total

    # 1900 ms. Time: O(N^2). Space: O(1) From discussion.
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i, num in enumerate(rating):
            lt_left = lt_right = gt_left = gt_right = 0
            for j, num2 in enumerate(rating):
                if num < num2 and i < j:
                    lt_left += 1
                if num > num2 and i < j:
                    gt_left += 1
                if num < num2 and i > j:
                    lt_right += 1
                if num > num2 and i > j:
                    gt_right += 1
            res += lt_left * gt_right + gt_left * lt_right
        return res

# @lc code=end
