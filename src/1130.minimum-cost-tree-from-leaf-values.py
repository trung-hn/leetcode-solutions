#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#

# @lc code=start
# TAGS: Dynamic Programming, Tree, Stack
# REVIEWME: Stack


class Solution:
    # 32 ms, 82.17%. Time: O(N^2). Space: O(N)
    def mctFromLeafValues(self, arr: List[int]) -> int:
        total = 0
        while len(arr) >= 2:
            i = arr.index(min(arr))
            total += min(arr[i - 1: i] + arr[i + 1: i + 2]) * arr.pop(i)
        return total

    # 32 ms, 82.17%. Time and Space: O(N)
    def mctFromLeafValues(self, arr: List[int]) -> int:
        total = 0
        stack = [float("inf")]
        for num in arr:
            while stack[-1] <= num:
                mid = stack.pop()
                total += mid * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            total += stack.pop() * stack[-1]
        return total
# @lc code=end
