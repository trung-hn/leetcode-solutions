#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#

# @lc code=start
# TAGS: Math, Sort
class Solution:
    # 180 ms, 84.15%. Time: O(NlogN). Space: O(N)
    def largestPerimeter(self, A: List[int]) -> int:
        def valid(a, b, c):
            return a + b > c and a + c > b and b + c > a
                    
        A.sort(reverse=True)
        for a, b, c in zip(A, A[1:], A[2:]):
            if valid(a, b, c):
                return a + b + c
        return 0
                    
# @lc code=end

