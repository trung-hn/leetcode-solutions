#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
# TAGS: Stack
class Solution:
    # Time and Space: O(N)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid < 0:
                while stack and 0 < stack[-1] < -asteroid:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == -asteroid:
                    stack.pop()
            else:
                stack.append(asteroid)
        return stack
# @lc code=end

