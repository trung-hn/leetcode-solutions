#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
# TAGS: Hash Table, Two Pointers, String, Sliding Window
import collections


class Solution:
    # 140 ms, 34.23%. Time and Space: O(T+S)
    def minWindow(self, s: str, t: str) -> str:
        counter = collections.Counter(t)
        seen = collections.Counter()
        match = set()
        window = "." * (len(s) + 1)
        ptr = 0
        for i, c in enumerate(s):  # O(S)
            seen[c] += 1
            # This char is in t
            if c in counter and seen[c] >= counter[c]:
                match.add(c)

            while len(match) == len(counter):
                # Get minium window
                if i + 1 - ptr < len(window):
                    window = s[ptr: i + 1]

                # Move left ptr
                seen[s[ptr]] -= 1
                if seen[s[ptr]] < counter[s[ptr]]:
                    match.discard(s[ptr])
                ptr += 1
        return "" if window[0] == '.' else window
# @lc code=end
