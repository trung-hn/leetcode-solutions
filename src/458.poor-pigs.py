#
# @lc app=leetcode id=458 lang=python3
#
# [458] Poor Pigs
#

# @lc code=start
# TAGS: Math
class Solution:
    # Time and Space: O(1)
    # Explanation from Stefan: https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # The important point is: pig can drink as many buckets as they want. 
        # Thus, we can assign each pig to a dimension
        trials = minutesToTest // minutesToDie + 1
        return ceil(math.log(buckets, trials))
        
        
        
# @lc code=end

