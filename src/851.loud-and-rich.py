#
# @lc app=leetcode id=851 lang=python3
#
# [851] Loud and Rich
#

# @lc code=start
# TAGS: DFS
# REVIEWME: DFS
class Solution:
    # 644 ms, 21.09%. Time and Space: O(N^2)
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = collections.defaultdict(list)
        for r, p in richer:
            graph[p].append(r)
        
        def dfs(i, visited):
            for person in graph[i]:
                visited.add(person)
                if person in self.richers:
                    visited |= self.richers[person]
                else:
                    dfs(person, visited)
        
        def get_loudest(target, quiet):
            loudest = quiet[target]
            arg = target
            for person in self.richers[target]:
                if quiet[person] < loudest:
                    loudest = quiet[person]
                    arg = person
            return arg
        
        self.richers = collections.defaultdict(set)
        ans = []
        for i in range(len(quiet)):
            if i not in self.richers: dfs(i, self.richers[i])
            ans.append(get_loudest(i, quiet))
        return ans
    
    # 436 ms, 93.20%. Time and Space: O(N^2). Clean solution from article
    def loudAndRich(self, richer, quiet):
        N = len(quiet)
        graph = [[] for _ in range(N)]
        for u, v in richer:
            graph[v].append(u)

        answer = [None] * N
        def dfs(node):
            if answer[node] is None:
                answer[node] = node
                for child in graph[node]:
                    rv = dfs(child)
                    if quiet[rv] < quiet[answer[node]]:
                        answer[node] = rv
            return answer[node]

        return map(dfs, range(N))
# @lc code=end

