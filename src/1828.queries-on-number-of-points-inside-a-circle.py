#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#

# @lc code=start


class Solution:
    # 2492 ms, 100%. Time: O(N*M). Space: O(M)
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for x, y, r in queries:
            cnt = sum((x - xp) ** 2 + (y - yp) ** 2 <=
                      r ** 2 for xp, yp in points)
            ans.append(cnt)
        return ans
# @lc code=end
