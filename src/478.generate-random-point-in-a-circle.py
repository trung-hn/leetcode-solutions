#
# @lc app=leetcode id=478 lang=python3
#
# [478] Generate Random Point in a Circle
#

# @lc code=start
# TAGS: Math, Random, Rejection Sampling
# REVIEWME: Math, Random, Rejection Sampling


class Solution:
    # Time and Space: O(1)
    def __init__(self, radius, x_center, y_center):
        self.r, self.x, self.y = radius, x_center, y_center

    def randPoint(self):
        theta = uniform(0, 2*pi)
        R = self.r*sqrt(uniform(0, 1))
        return [self.x + R*cos(theta), self.y + R*sin(theta)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
# @lc code=end
