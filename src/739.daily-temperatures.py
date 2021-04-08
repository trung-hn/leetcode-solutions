#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
# TAGS: Hash Table, Stack


class Solution:
    # 504 ms, 75%. Time and Space: O(N)
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        results = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                prev = stack.pop()
                results[prev] = i - prev
            stack.append(i)
        return results
# @lc code=end
