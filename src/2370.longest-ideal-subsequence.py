#
# @lc app=leetcode id=2370 lang=python3
#
# [2370] Longest Ideal Subsequence
#


# @lc code=start
# TAGS: Hash Table, String, Dynamic Programming
# REVIEWME: Dynamic Programming


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        counter = [0] * 26
        for c in s:
            i = ord(c) - ord("a")
            for n in range(max(i - k, 0), min(i + k, 25) + 1):
                counter[i] = max(counter[i], counter[n])
            counter[i] += 1
        return max(counter)


# @lc code=end
