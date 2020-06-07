#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
# TAGS: Greedy
# REVIEWME: Clever solution
class Solution:
    # 96 ms, 87.9%. Time: O(N^2). Space: O(N)
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        rv = []
        for h, k in people:
            rv.insert(k, [h,k])
        return rv
# @lc code=end

