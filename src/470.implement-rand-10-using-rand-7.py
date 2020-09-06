#
# @lc app=leetcode id=470 lang=python3
#
# [470] Implement Rand10() Using Rand7()
#

# @lc code=start
# TAGS: Math
# REVIEWME: Math, Design
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    # From discussion: https://leetcode.com/problems/implement-rand10-using-rand7/discuss/816210/Python-rejection-sampling-2-lines-explained
    # This is related to geometric distribution.
    def rand10(self):
        c = (rand7() - 1)*7 + rand7() - 1
        return self.rand10() if c >= 40 else (c % 10) + 1
        
# @lc code=end

