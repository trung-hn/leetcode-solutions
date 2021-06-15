#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#

# @lc code=start
# TAGS: DFS, Dynamic Programming
# REVIEWME: DFS, Dynamic Programming


class Solution:

    # LTE: O(N!)
    def makesquare(self, matchsticks: List[int]) -> bool:
        target = sum(matchsticks) // 4
        self.rv = False

        def dfs(total=0, visited=set(), cnt=0):
            # print(visited, total, target)
            if total == target:
                cnt += 1
                total = 0
            if cnt == 4:
                self.rv = True
            for i in range(len(matchsticks)):
                if i in visited:
                    continue
                visited.add(i)
                dfs(total + matchsticks[i], visited, cnt)
                visited.discard(i)

        dfs()
        return self.rv

    # 232 ms, 60.94%. Time: O(4^N). Space: O(4^N).
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        target = sum(matchsticks) // 4

        self.rv = False
        visited = set()

        def dfs(t1=0, t2=0, t3=0, t4=0, i=0):
            # Short circuit
            if max(t1, t2, t3, t4) > target:
                return

            # Memoization
            key = tuple(sorted([t1, t2, t3, t4]))
            if key in visited:
                return
            visited.add(key)

            # Base Case
            if i == len(matchsticks):
                return t1 == t2 == t3 == t4

            # Recursion
            return dfs(t1 + matchsticks[i], t2, t3, t4, i + 1) \
                or dfs(t1, t2 + matchsticks[i], t3, t4, i + 1) \
                or dfs(t1, t2, t3 + matchsticks[i], t4, i + 1) \
                or dfs(t1, t2, t3, t4 + matchsticks[i], i + 1)
        return dfs()

# @lc code=end
