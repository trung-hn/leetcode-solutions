#
# @lc app=leetcode id=880 lang=python3
#
# [880] Decoded String at Index
#

# @lc code=start
# TAGS: Stack
class Solution:
    # 20 ms, 97.97%. Time: O(N). Space: O(N)
    def decodeAtIndex(self, S: str, K: int) -> str:
        def f(S, K):
            curr = 0
            for c in S:
                if c.isdigit():
                    if curr * int(c) >= K:
                        return f(S, K % curr) if K % curr else f(S, curr)
                    curr *= int(c)
                else:
                    curr += 1
                if curr == K: return c
        return f(S,K)

    # Same as above but Iteratively
    def decodeAtIndex(self, S: str, K: int) -> str:
        while 1:
            curr = 0
            for c in S:
                if c.isdigit():
                    if curr * int(c) >= K:
                        K = K % curr if K % curr else curr
                        break
                    curr *= int(c)
                else:
                    curr += 1
                if curr == K: return c

    # Solution from article. Time: O(N). Space: O(1)
    def decodeAtIndex(self, S, K):
        size = 0
        # Find size = length of decoded string
        for c in S:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1

        for c in reversed(S):
            K %= size
            if K == 0 and c.isalpha():
                return c

            if c.isdigit():
                size /= int(c)
            else:
                size -= 1
# @lc code=end

