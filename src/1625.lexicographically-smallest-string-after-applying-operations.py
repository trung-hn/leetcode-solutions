#
# @lc app=leetcode id=1625 lang=python3
#
# [1625] Lexicographically Smallest String After Applying Operations
#

# @lc code=start
# TAGS: BFS, DFS


class Solution:
    """
    We Can bruteforce this problem because we notice that 10a = 0a
    """
    # 136 ms, 92.93%. Time: O(N^2). Space: O(N)

    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
                # Try all shifting positions and compare
        def get_smaller(ans, s):
            for _ in range(len(s)):
                s = s[b:] + s[:b]
                ans = min(ans, s)
            return ans

            # Add number to just odd or even digits.
        def add_a(temp, odd=True):
            rv = [str((int(c) + a) % 10) if i %
                  2 == odd else c for i, c in enumerate(temp)]
            return "".join(rv)

        ans = "9" * len(s)
        odd = s
        # Shift Odd digits
        for _ in range(10):
            odd = add_a(odd, True)
            even = odd

            # Shift Even digits if applicable
            for _ in range(10) if b % 2 else range(1):
                ans = get_smaller(ans, even)
                even = add_a(even, False)
        return ans

    # 1440 ms, 68.48%. Same complexity but slow because of overheads

    def findLexSmallestString1(self, s: str, a: int, b: int) -> str:
        def add(s, a):
            return "".join(str((int(c) + a) % 10) if i % 2 else c for i, c in enumerate(s))

        def rotate(s, b):
            return s[b:] + s[:b]

        visited = set()
        q = [s]
        for s in q:
            if s in visited:
                continue
            visited.add(s)
            q.append(add(s, a))
            q.append(rotate(s, b))

        return min(visited)


# @lc code=end
