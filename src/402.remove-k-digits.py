#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#

# @lc code=start
# TAGS: Greedy
# REVIEWME:
class Solution:
    # 32 ms, 90.71%.
    def removeKdigits(self, num: str, k: int) -> str:
        rv = []
        for n in num:
            while rv and rv[-1] > n and k:
                rv.pop()
                k -= 1
            rv.append(n)
        if k: rv = rv[:-k]
        return str(int("".join(rv))) if rv else "0"
# @lc code=end

