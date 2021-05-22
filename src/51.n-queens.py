#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
# TAGS: Backtracking


class Solution:
    # 80 ms, 57.03%. Time: O(N!). Space: O(N^2)
    def solveNQueens(self, n: int) -> List[List[str]]:
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
                ans.append(["".join(row) for row in temp])
                return

            for i in range(n):
                if not_available(step, i, used):
                    continue

                # add to used list
                used.add((step, i))
                used.add(i)
                temp[step][i] = "Q"
                dfs(step + 1)
                temp[step][i] = "."

                # remove from used list
                used.discard(i)
                used.discard((step, i))

        temp = [["."] * n for _ in range(n)]
        ans = []
        dfs()
        return ans
# @lc code=end
