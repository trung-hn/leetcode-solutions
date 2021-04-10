#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start
# TAGS: BFS, DFS


class Solution:
    # 776 ms, 38.71%. Time and Space: O(R*C)
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        R, C = len(matrix), len(matrix[0])
        zeroes = [(r, c) for r in range(R)
                  for c in range(C) if matrix[r][c] == 0]

        step = 0
        visited = set()
        while zeroes:
            nxt = set()
            for r, c in zeroes:

                # check if visited
                if (r, c) in visited:
                    continue
                visited.add((r, c))

                # Step away from nearest 0
                matrix[r][c] = step

                # Add neighbors to nxt
                for x, y in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if 0 <= x < R and 0 <= y < C and (x, y) not in visited:
                        nxt.add((x, y))
            step += 1
            zeroes = nxt
        return matrix
# @lc code=end
