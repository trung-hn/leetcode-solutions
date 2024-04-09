#
# @lc app=leetcode id=3090 lang=python3
#
# [3090] Maximum Length Substring With Two Occurrences
#

# @lc code=start
# TAGS: Hash Table, String, Sliding Window
from collections import Counter


class Solution:
    # Time: O(N) Space: O(1)
    def maximumLengthSubstring(self, s: str) -> int:
        counter = Counter()
        ans = ptr = 0
        for i, c in enumerate(s):
            counter[c] += 1
            while counter[c] > 2:
                counter[s[ptr]] -= 1
                ptr += 1
            ans = max(ans, i - ptr + 1)
        return ans


# @lc code=end
