#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
# TAGS: String, Sliding Window
class Solution:
    # 180 ms, 82.22%. Time: O(N). Space: O(1)
    # Add, Check, Subtract
    def maxVowels(self, s: str, k: int) -> int:
        max_freq = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] in "aeiou":
                cnt += 1
            max_freq = max(max_freq, cnt)
            if i >= k-1 and s[i - (k - 1)] in "aeiou":
                cnt -= 1
        return max_freq

    # Similar, just different order of execution. 
    def maxVowels(self, s: str, k: int) -> int:
        max_freq = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] in "aeiou":
                cnt += 1
            if i >= k and s[i - k] in "aeiou":
                cnt -= 1
            max_freq = max(max_freq, cnt)
        return max_freq

# @lc code=end

