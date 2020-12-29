#
# @lc app=leetcode id=754 lang=python3
#
# [754] Reach a Number
#

# @lc code=start
# TAGS: Math
# REVIEWME: Math
class Solution(object):
    """
    Look at article for explanation:
    let S = 1 + 2 + ... + k >= target
    delta = S - target
    if delta is even. we can switch some 1 number between {1, k} to negative to offset this
    if delta is odd. we can add (k + 1):
        if even: ans = k + 1 (back to earlier problem)
        if odd again: this means k is even. ans = k + 1 + 1
    """
    # Time: O(logN). Space: O(1)
    def reachNumber(self, target):
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        return k if target % 2 == 0 else k + 1 + k%2
# @lc code=end

