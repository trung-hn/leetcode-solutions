#
# @lc app=leetcode id=3085 lang=python3
#
# [3085] Minimum Deletions to Make String K-Special
#


# @lc code=start
class Solution:
    # Time: O(N). Space: O(26)
    def minimumDeletions(self, word: str, k: int) -> int:
        def remove_except(lower, upper):
            total = 0
            for c in counter.values():
                if c < lower:
                    total += c
                if c > upper:
                    total += c - upper
            return total

        counter = collections.Counter(word)
        ans = float("inf")
        for c in counter.values():
            deletions = remove_except(c, c + k)
            ans = min(ans, deletions)
        return ans


# @lc code=end
