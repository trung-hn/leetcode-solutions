#
# @lc app=leetcode id=1750 lang=python3
#
# [1750] Minimum Length of String After Deleting Similar Ends
#

# @lc code=start
# TAGS: Two Pointers


class Solution:
    # 148 ms, 39.20%. Time: O(N). Space: O(1)
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                break
            elif left + 1 == right:
                return 0
            elif s[left + 1] == s[right]:
                left += 1
            elif s[left] == s[right - 1]:
                right -= 1
            else:
                left += 1
                right -= 1
        return right - left + 1
# @lc code=end
