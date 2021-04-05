#
# @lc app=leetcode id=1781 lang=python3
#
# [1781] Sum of Beauty of All Substrings
#

# @lc code=start
# TAGS: Hash Table, String


class Solution:
    # 2880 ms, 68.61%. Time: O(N^2). Space: O(1)
    def beautySum(self, s: str) -> int:
        def get_min_max_diff(counter):
            return max(counter.values()) - min(counter.values())

        total = 0
        for window in range(1, len(s)):
            counter = collections.Counter(s[:window])
            for i in range(window, len(s)):
                counter[s[i]] += 1
                total += get_min_max_diff(counter)

                # Remove first value
                if i < window:
                    continue
                counter[s[i - window]] -= 1
                if counter[s[i - window]] == 0:
                    del counter[s[i - window]]
        return total
# @lc code=end
