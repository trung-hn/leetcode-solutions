#
# @lc app=leetcode id=1996 lang=python3
#
# [1996] The Number of Weak Characters in the Game
#

# @lc code=start
# TAGS: Array, Stack, Greedy, Sorting, Monotonic Stack
# REVIEWME: Sorting, Monotonic Stack
class Solution:
    # 3704 ms, 39.59%. Time: O(NlogN). Space: O(N)
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[-1]))
        stack = []
        for _, y in properties:
            while stack and stack[-1] < y:
                stack.pop()
            stack.append(y)
        return len(properties) - len(
            stack
        )  # Essentially, cnt += 1 every time stack.pop()


# @lc code=end
