#
# @lc app=leetcode id=735 lang=python3
#
# [735] Asteroid Collision
#

# @lc code=start
# TAGS: Stack


class Solution:
    # Pythonic
    # 108 ms, 26.73%. Time and Space: O(N).
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                prev = stack.pop()

                # Both got destroyed
                if prev + asteroid == 0:
                    break

                # Else get the bigger one by size
                asteroid = max(asteroid, prev, key=abs)
            else:
                stack.append(asteroid)
        return stack

    # Any language
    # 96 ms, 73.31%. Time and Space: O(N)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and 0 < stack[-1]:
                prev = stack.pop()

                # Both got destroyed
                if abs(asteroid) == abs(prev):
                    asteroid = 0
                # The biggest one by size
                elif abs(asteroid) < abs(prev):
                    asteroid = prev
            if asteroid:
                stack.append(asteroid)
        return stack
# @lc code=end
