#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#

# @lc code=start
# TAGS: Greedy, Dynamic Programming
# REVIEWME: Greedy
class Solution:
    # TLE
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        self.ans = 0
        visited = collections.defaultdict(int)
        @functools.lru_cache(None)
        def dfs(prev=0, i=0, sofar=0):
            if i >= len(pairs):
                self.ans = max(self.ans, sofar)
                return
            for j in range(i, len(pairs)):
                start, end = pairs[j]
                if start > prev:
                    dfs(end, j + 1, sofar + 1)
        
        dfs(float("-inf"), 0)
        return self.ans
    
    # Time Limit Exceeded. DP. Time: O(N^2). Space: O(N)
    def findLongestChain(self, pairs):
        pairs.sort()
        dp = [1] * len(pairs)

        for j in xrange(len(pairs)):
            for i in xrange(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)
    
    # Greedy. Time: O(NlogN). Space: O(N)
    # We choose the next value with lowest second coordinate. 
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        curr, ans = float("-inf"), 0
        for start, end in pairs:
            if curr < start:
                curr = end
                ans += 1
        return ans
# @lc code=end

