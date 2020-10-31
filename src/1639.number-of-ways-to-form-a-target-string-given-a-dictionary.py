#
# @lc app=leetcode id=1639 lang=python3
#
# [1639] Number of Ways to Form a Target String Given a Dictionary
#

# @lc code=start
# TAGS: Dynamic Programming
# REVIEWME: Dynamic Programming
class Solution:
    # LTE.
    # Done in contest. Very close to working solution. Problems:
    # 1. sofar gets so big that it takes time to calculate and pass to next recursion
    # 2. we loop through all k instead of only until M - (N - i) + 1
    # 3. we are not MODding sofar as soon as we can
    def numWays(self, words: List[str], target: str) -> int:
        MOD = (10**9 + 7)
        M = len(words[0]); N = len(target)
        counter_by_index = [collections.Counter() for _ in range(M)]
        for word in words:
            for i, c in enumerate(word):
                counter_by_index[i][c] += 1
        
        @functools.lru_cache(None)
        def dfs(start, i, target, sofar=1):
            if i >= N:
                return sofar
            
            rv = 0
            for k in range(start, M):
                cnt = counter_by_index[k][target[i]]
                if cnt == 0: continue
                rv += dfs(k + 1, i + 1, target, cnt*sofar)
            return rv
        self.ans = dfs(0, 0, target)
        return self.ans % MOD
    
    # Similar to above but optimized
    # with modding at each step: 4292 ms, 20%.
    # without modding at each step: 5360 ms, 20%.
    # Time and Space: O(M*N).
    def numWays(self, words: List[str], target: str) -> int:
        MOD = (10**9 + 7)
        M = len(words[0]); N = len(target)
        counter_by_index = [collections.Counter() for _ in range(M)]
        for word in words:
            for i, c in enumerate(word):
                counter_by_index[i][c] += 1
                
        @functools.lru_cache(None)
        def dfs(start, i):
            if i >= N: return 1
            rv = 0
            for k in range(start, M - (N - i) + 1):
                cnt = counter_by_index[k][target[i]]
                if cnt == 0: continue
                rv += dfs(k + 1, i + 1) * cnt
                rv %= MOD
            return rv
        return dfs(0, 0) % MOD
    
    # 2768 ms, 20.00%. Time and Space: O(M*N). 
    # Similar to discussion: https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/discuss/917694/Python-Top-Down-DP-Clean-and-Concise-O(m*n)
    def numWays1(self, words: List[str], target: str) -> int:
        MOD = (10**9 + 7)
        M = len(words[0]); N = len(target)
        counter_by_index = [collections.Counter() for _ in range(M)]
        for word in words:
            for i, c in enumerate(word):
                counter_by_index[i][c] += 1
                
        @functools.lru_cache(None)
        def dfs(k, i):
            if i >= N: return 1
            if k >= M: return 0
            rv = dfs(k + 1, i)
            cnt = counter_by_index[k][target[i]]
            if cnt > 0:
                rv += dfs(k + 1, i + 1) * cnt
                rv %= MOD
            return rv
        return dfs(0, 0) % MOD
    
    # 1568 ms, From lee215
    def numWays(self, words, target):
        n, mod = len(target), 10**9 + 7
        res = [1] + [0] * n
        for i in range(len(words[0])):
            count = collections.Counter(w[i] for w in words)
            for j in range(n - 1, -1, -1):
                res[j + 1] += res[j] * count[target[j]] % mod
        return res[n] % mod
# @lc code=end

