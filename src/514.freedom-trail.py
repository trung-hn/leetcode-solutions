#
# @lc app=leetcode id=514 lang=python3
#
# [514] Freedom Trail
#


# @lc code=start
# TAGS: String, Dynamic Programming, Depth-First Search, Breadth-First Search
# REVIEWME: Dynamic Programming
import functools, collections


class Solution:
    # Memoization. Time and Space: O(N*M)
    def findRotateSteps(self, ring: str, key: str) -> int:
        def steps(ring_ptr, p):
            normal = abs(ring_ptr - p)
            return min(normal, len(ring) - normal)

        @functools.cache
        def dfs(ring_ptr=0, key_ptr=0):
            if key_ptr == len(key):
                return 0
            rv = float("inf")
            for p in pos[key[key_ptr]]:
                dist = steps(ring_ptr, p)
                rv = min(rv, dfs(p, key_ptr + 1) + dist)
            return rv

        pos = collections.defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)
        return dfs(0, 0) + len(key)

    # DP. Time and Space: O(N*M). Can still optimize for space.
    def findRotateSteps(self, ring: str, key: str) -> int:
        def steps(ring_ptr, p):
            normal = abs(ring_ptr - p)
            return min(normal, len(ring) - normal)

        pos = collections.defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)

        # Init base case (similar to base case in recursion)
        dp = collections.defaultdict(lambda: float("inf"))
        for i in range(len(ring)):
            dp[(i, len(key))] = 0

        # Recursion in interative format
        for key_ptr in reversed(range(len(key))):
            for ring_ptr in range(len(ring)):
                for p in pos[key[key_ptr]]:
                    dist = steps(ring_ptr, p)
                    dp[(ring_ptr, key_ptr)] = min(
                        dp[(ring_ptr, key_ptr)], dp[(p, key_ptr + 1)] + dist
                    )
        return dp[(0, 0)] + len(key)


# @lc code=end
