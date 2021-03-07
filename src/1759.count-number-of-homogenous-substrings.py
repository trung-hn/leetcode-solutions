#
# @lc app=leetcode id=1759 lang=python3
#
# [1759] Count Number of Homogenous Substrings
#

# @lc code=start
# TAGS: String, Greedy


class Solution:
    # 168 ms, 68.75%. Time: O(N). Space: O(1)
    def countHomogenous(self, s: str) -> int:
        def cal(n):
            return n * (n + 1) // 2
        MOD = 10**9 + 7
        total = ptr = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] != s[ptr]:
                total = (total + cal(i - ptr)) % MOD
                ptr = i
        return total

# @lc code=end
