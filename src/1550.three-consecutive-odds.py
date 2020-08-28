#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
# TAGS: Array
class Solution:
    # 52 ms, 58.75 %. Time: O(N). Space: O(1)
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cnt = 0
        for n in arr:
            if n % 2: 
                cnt += 1
            else:
                cnt = 0
            if cnt == 3: return True
        return False
            
# @lc code=end

