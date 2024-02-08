#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#


# @lc code=start
# TAGS: Math, Dynamic Programming, BFS
class Solution:
    # 4208 ms, 47%. Populate from left to right at each square numbers.
    def numSquares(self, n: int) -> int:
        if not n:
            return 0
        square_nums = [n**2 for n in range(int(n**0.5) + 1)]
        dp_nums = [0] + [float(inf)] * n
        for num in square_nums:
            for i in range(num, len(dp_nums)):
                dp_nums[i] = min(
                    dp_nums[i], 1 + dp_nums[i - num]
                )  # because dp_nums[num] == 1
        return dp_nums[n]

    # 488 ms, 67.2%
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        square_nums = set([n**2 for n in range(int(n**0.5) + 1)])
        visited = set()
        q = [(n, 0)]
        for val, depth in q:
            if val in visited:
                continue
            visited.add(val)
            for sq in square_nums:
                if sq == val:
                    return depth + 1
                elif sq < val:
                    q.append([val - sq, depth + 1])

    # 3084 ms, 51.30% A lot slower just by check val == 0 at next depth.
    def numSquares1(self, n: int) -> int:
        square_nums = set([n**2 for n in range(int(n**0.5) + 1)])
        visited = set()
        q = [(n, 0)]
        for val, depth in q:
            if val == 0:
                return depth
            if val in visited:
                continue
            visited.add(val)
            for sq in square_nums:
                if sq <= val:
                    q.append([val - sq, depth + 1])

    # 3084 ms, 51.30% A lot slower just by check val == 0 at next depth.
    def numSquares2(self, n: int) -> int:
        square_nums = set([n**2 for n in range(int(n**0.5) + 1)])
        visited = set()
        q = [(n, 0)]
        for val, depth in q:
            if val == 0:
                return depth
            if val in visited or val < 0:
                continue
            visited.add(val)
            for sq in square_nums:
                q.append([val - sq, depth + 1])

    # Redo in 2024.
    # Memoization:
    # 2953 ms. 35.86%
    def numSquares(self, n: int) -> int:
        """
        The idea is to recursively select i -1, -4, -9, ...
        because +1, +4, +9 are the fewest increment (1)
        """
        squares = [i * i for i in reversed(range(1, int(n**0.5) + 1))]

        @functools.cache
        def dfs(num):
            rv = float("inf")
            for sq in squares:
                if sq > num:
                    continue
                elif sq == num:
                    return 1
                else:
                    rv = min(rv, dfs(num - sq) + 1)
            return rv

        return dfs(n)

    # 2235 ms.
    def numSquares(self, n: int) -> int:
        """Same as above but dp"""
        sqs = [i * i for i in range(1, int(n**0.5) + 1)]
        mem = {0: 0}
        for i in range(1, n + 1):
            val = float("inf")
            for sq in sqs:
                if sq > i:
                    break
                val = min(val, mem[i - sq] + 1)
            mem[i] = val
        return mem[i]


# @lc code=end
