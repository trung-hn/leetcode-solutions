#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
# TAGS: Backtracking


class Solution:
    # 72 ms, 43.92%. Time: O(N!). Space: O(N^2)
    def totalNQueens(self, n: int) -> int:
        def not_available(step, i, used):
            if i in used:
                return True
            for j in range(1, step + 1):
                if (step - j, i - j) in used:
                    return True
                if (step - j, i + j) in used:
                    return True
            return False

        def dfs(step=0, used=set()):
            if step == n:
                return 1

            rv = 0
            for i in range(n):
                if not_available(step, i, used):
                    continue

                # add to used list
                used.add((step, i))
                used.add(i)
                rv += dfs(step + 1)

                # remove from used list
                used.discard(i)
                used.discard((step, i))
            return rv
        return dfs()

# @lc code=end
