#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
# TAGS: Sort
class Solution:
    # 168 ms, 78.59%. Time: O(NlogN). Space: O(N) because of Sort
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - pos) / sp for pos, sp in zip(position, speed)]
        stack = []
        for _, t in sorted(zip(position, time)):
            while stack and stack[-1] <= t:
                stack.pop()
            stack.append(t)
        return len(stack)
# @lc code=end

