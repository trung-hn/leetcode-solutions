#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start
# TAGS: Array
class Solution:
    # 588 ms, 14.92%. Time and Space: O(N)
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_from_left = []
        max_from_right = []
        max_left = max_right = 0
        for i in range(len(values)):
            max_from_left.append(max_left)
            max_left = max(values[i], max_left) - 1
            
            max_from_right.append(max_right)
            max_right = max(values[~i], max_right) - 1
        
        max_from_right.reverse()
        ans = 0
        for val, left, right in zip(values, max_from_left, max_from_right):
            ans = max([ans, val + left, val + right])
        return ans
    
    # Cleaner solution
    # if a is max_from_left of b, then b is max_from_right of a => we only need 1 max_from
    # because we only have 1 max_from, we can calculate ans on the fly as soon as we have max_from
    # 468 ms, 74.92%. Time: O(N). Space: O(1)
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = max_left = 0
        for val in values:
            ans = max(ans, val + max_left)
            max_left = max(val, max_left) - 1
        return ans
# @lc code=end

