#
# @lc app=leetcode id=1647 lang=python3
#
# [1647] Minimum Deletions to Make Character Frequencies Unique
#

# @lc code=start
# TAGS: Greedy, Sort
class Solution:
    # 104 ms, 97.48%
    def minDeletions(self, s: str) -> int:
        counter = collections.Counter(s)
        used = set(); ans = 0
        for _, freq in counter.items():
            while freq > 0 and freq in used:
                freq -= 1
                ans += 1
            used.add(freq)
        return ans
# @lc code=end

