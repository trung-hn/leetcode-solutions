#
# @lc app=leetcode id=1839 lang=python3
#
# [1839] Longest Substring Of All Vowels in Order
#

# @lc code=start
# TAGS: Two Pointers, String


class Solution:
    # 852 ms, 48.60%. Time: O(N). Space: O(1)
    def longestBeautifulSubstring(self, word: str) -> int:
        ans = 0
        total = 1
        visited = {word[0]}
        for c1, c2 in zip(word, word[1:]):
            if c1 > c2:
                total = 0
                visited = set()
            total += 1
            visited.add(c2)
            if len(visited) == 5:
                ans = max(ans, total)
        return ans

    # 868 ms, 47.37%. Time: O(N). Space: O(1). Same algorithm but 2 pointers
    def longestBeautifulSubstring(self, word: str) -> int:
        left = ans = 0
        visited = {word[0]}
        for right in range(1, len(word)):
            if word[right - 1] > word[right]:
                left = right
                visited = set()
            visited.add(word[right])
            if len(visited) == 5:
                ans = max(ans, right - left + 1)
        return ans
# @lc code=end
