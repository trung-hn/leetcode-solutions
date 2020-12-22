#
# @lc app=leetcode id=910 lang=python3
#
# [910] Smallest Range II
#

# @lc code=start
# TAGS: Math, Greedy
# REVIEWME: Math, Greedy
class Solution:
    # linear scan
    # from article: consider i at A[i] is the last value goes up,
    # this means only index at 0, i, i + 1, and -1 matters in the boundary
    # the rest are within these 4
    # Time: O(NlogN). Space: O(N)
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        ans = A[-1] - A[0] # Case where all values increase
        for num1, num2 in zip(A, A[1:]):
            # i is the last number that goes up
            lower = min(A[0] + K, num2 - K)
            higher = max(A[-1] - K, num1 + K)
            ans = min(ans, higher - lower)
        return ans
# @lc code=end

