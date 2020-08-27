#
# @lc app=leetcode id=1556 lang=python3
#
# [1556] Thousand Separator
#

# @lc code=start
class Solution:
    # 32 ms, 81.48%. Time and Space: O(N)
    def thousandSeparator(self, n: int) -> str:
        n = str(n)
        start = len(n) % 3
        rv = [n[:start]] if start else []
        for i in range(start, len(n), 3):
            rv.append(n[i:i+3])
        return ".".join(rv)
# @lc code=end

