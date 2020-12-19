#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
# TAGS: Array
class Solution:
    # 56 ms, 47.55%. Time: O(N). Space: O(1)
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        lowest_second = float("inf")
        for num in nums:
            if second < num or lowest_second < num:
                return True
            
            if num < first:
                lowest_second = min(lowest_second, second)
                first = num
                second = float("inf")
            elif first < num < second:
                second = num
        return False
    
    # 56 ms, 47.55%. From discussion. 
    # Same idea but cleaner because we use second to keep track of lowest_second
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        for num in nums:
            if num < first:
                first = num
            elif first < num < second:
                second = num
            elif second < num:
                return True
        return False
# @lc code=end

