#
# @lc app=leetcode id=1632 lang=python3
#
# [1632] Rank Transform of a Matrix
#

# @lc code=start
# TAGS: Array, Greedy, Union Find, Graph, Topological Sort, Matrix
# REVIEWME: Union Find, Topological Sort


class Solution:
    # 2060 ms, Time: O(NlogN). Space: O(N). N = R*C
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:

        class UF:
            def __init__(self, N):
                self.parent = list(range(N))
                self.visited = set()

            def union(self, x, y):
                self.parent[self.find(y)] = self.find(x)
                self.visited.add(x)
                self.visited.add(y)

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def get_groups(self):
                groups = collections.defaultdict(list)
                for i in self.visited:
                    groups[self.find(i)].append(i)
                return groups

        R, C = len(matrix), len(matrix[0])

        data = collections.defaultdict(list)
        for r in range(R):
            for c in range(C):
                data[matrix[r][c]].append((r, c))

        # Notice that we use 1D array to store rank of both rows and columns. offset by R
        ranks = [0] * (R + C)
        for k in sorted(data):
            uf = UF(R + C)

            # Union column and row together.
            # This means they will have the same rank for this value
            for r, c in data[k]:
                uf.union(r, c + R)

            for group in uf.get_groups().values():
                # get max rank of all involved rows and columns
                max_rank = max(ranks[i] for i in group)

                # assign new rank to involved rows and columns
                for i in group:
                    ranks[i] = max_rank + 1

            # Assign new rank to all cells of this value
            for r, c in data[k]:
                matrix[r][c] = ranks[r]

        return matrix
# @lc code=end
