#
# @lc app=leetcode id=1974 lang=python3
#
# [1974] Minimum Time to Type Word Using Special Typewriter
#

# @lc code=start
# TAGS: String, Greedy


class Solution:
    # 28 ms, Time: O(N). Space: O(1)
    def minTimeToType(self, word: str) -> int:

        def get_min_dist(a, b):
            dist = abs(ord(b) - ord(a))
            return min(dist, 26 - dist)

        ans = 0
        prev = 'a'
        for c in word:
            ans += get_min_dist(prev, c) + 1
            prev = c
        return ans

# @lc code=end
