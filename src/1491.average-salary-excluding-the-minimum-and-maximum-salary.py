#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
class Solution:
    # 32 ms 78.72%. Time: O(N). Space: O(1)
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
        
# @lc code=end

