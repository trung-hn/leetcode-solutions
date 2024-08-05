#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#


# @lc code=start
# TAGS: String, Binary Search, Sliding Window, Prefix Sum
class Solution:
    # Time: O(N^2). Space: O(N)
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = [abs(ord(c1) - ord(c2)) for c1, c2 in zip(s, t)]
        ans = 0
        for left in range(len(s)):
            total = 0
            for right in range(left, len(s)):
                total += diff[right]
                if total <= maxCost:
                    ans = max(ans, right - left + 1)
        return ans

    # Time: O(N). Space: O(N)
    def equalSubstring2(self, s: str, t: str, maxCost: int) -> int:
        diff = [abs(ord(c1) - ord(c2)) for c1, c2 in zip(s, t)]
        left = total = ans = 0
        for right in range(len(t)):
            total += diff[right]
            while total > maxCost:
                total -= diff[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


# @lc code=end
