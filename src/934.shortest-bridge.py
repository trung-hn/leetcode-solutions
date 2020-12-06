#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start
# TAGS: BFS, DFS
class Solution:

    # Helper function used by both
    def change_island_to_minus_1(self, A):
        def dfs(r, c):
            A[r][c] = -1
            for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if  0 <= x < R and 0 <= y < C and A[x][y] == 1:
                    dfs(x, y)
                    
        R, C = len(A), len(A[0])
        for r in range(R):
            for c in range(C):
                if A[r][c] == 1:
                    dfs(r, c)
                    return A

    # 3352 ms, 5.02%. DFS
    def shortestBridge(self, A: List[List[int]]) -> int:
        def dfs(r, c, depth=-1):
            if depth >= depth_matrix[r][c]: return
            depth_matrix[r][c] = depth
            # if depth >= self.ans: return
            if A[r][c] == 1:
                self.ans = min(self.ans, depth)
                return

            for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if  0 <= x < R and 0 <= y < C and A[x][y] != -1:
                    dfs(x, y, depth + 1)
        
        self.ans = float("inf")
        R, C = len(A), len(A[0])
        depth_matrix = [[R] * R for _ in range(R)]
        A = self.change_island_to_minus_1(A)
        for r in range(R):
            for c in range(C):
                if A[r][c] == -1:
                    dfs(r, c)
        return self.ans
        
    # 416 ms, 60.08%. BFS. Pay attention to how we improve times by 10 fold just by changing A "1 depth earlier."
    def shortestBridge(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        A = self.change_island_to_minus_1(A)
        q = collections.deque([(r, c, 0) for r in range(R) for c in range(C) if A[r][c] == -1])
        while q:
            r, c, depth = q.popleft()
            A[r][c] = -1
            for x, y in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
                if  0 <= x < R and 0 <= y < C:
                    if A[x][y] == 1:
                        return depth
                    elif A[x][y] == 0:
                        A[x][y] = -1 # although we do this in the next step, remove this will make it extremely slow.
                        q.append((x, y, depth + 1))
# @lc code=end

