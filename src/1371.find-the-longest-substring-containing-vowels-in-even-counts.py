#
# @lc app=leetcode id=1371 lang=python3
#
# [1371] Find the Longest Substring Containing Vowels in Even Counts
#

# @lc code=start
# TAGS: String
# REVIEWME: String, Bit Manipulation


class Solution:
    # 444 ms, 64.89%. Time: O(N). Space: O(N)
    def findTheLongestSubstring(self, s: str) -> int:
        cnt = [0, 0, 0, 0, 0]
        visited = {tuple(cnt): [-1]}
        for i, c in enumerate(s):
            if c in "aeoiu":
                cnt["aeoiu".find(c)] ^= 1
            visited.setdefault(tuple(cnt), []).append(i)
        return max(val[-1] - val[0] for val in visited.values())

    # 336 ms, 83.51%. Time: O(N). Space: O(N).
    # Use bit mask instead. Very clever
    def findTheLongestSubstring(self, s: str) -> int:
        cnt = 0
        visited = {cnt: [-1]}
        for i, c in enumerate(s):
            if c in "aeoiu":
                cnt ^= 1 << "aeoiu".find(c)
                # cur ^= (1 << ('aeiou'.find(c) + 1)) >> 1 # we can use this for chars not vowels as well
            visited.setdefault(cnt, []).append(i)
        return max(val[-1] - val[0] for val in visited.values())
# @lc code=end
