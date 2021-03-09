#
# @lc app=leetcode id=1765 lang=python3
#
# [1765] Map of Highest Peak
#

# @lc code=start
# TAGS: BFS, Graph


class Solution:
    # 4676 ms, 20%. Time: O(N*M). Space: O(N*M)
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R = len(isWater)
        C = len(isWater[0])

        waters = [(r, c, 0) for r in range(R)
                  for c in range(C) if isWater[r][c]]
        ans = [[0] * C for _ in range(R)]
        visited = set()
        for r, c, h in waters:
            if (r, c) in visited:
                continue
            visited.add((r, c))
            ans[r][c] = h
            for x, y in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                if 0 <= x < R and 0 <= y < C and (x, y) not in visited:
                    waters.append((x, y, h + 1))
        return ans

    # 3644 ms, 00%. Slight tweak to make it more efficient
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        R = len(isWater)
        C = len(isWater[0])

        waters = [(r, c, 0) for r in range(R)
                  for c in range(C) if isWater[r][c]]
        ans = [[0 if val else -1 for val in row] for row in isWater]
        visited = set()
        for r, c, h in waters:
            for x, y in (r-1, c), (r+1, c), (r, c-1), (r, c+1):
                if 0 <= x < R and 0 <= y < C and ans[x][y] == -1:
                    ans[x][y] = h + 1
                    waters.append((x, y, h + 1))
        return ans
# @lc code=end
