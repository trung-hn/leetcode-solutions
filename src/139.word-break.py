#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
# TAGS: Dynamic Programming
# REVIEWME: Dynamic Programming, BFS, DFS, Pythonic
import collections, functools
class Trie():
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.end = False

class Solution:
    # 36 ms, 85.35%. Write this myself. Trie and recursive. 
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.ans = False
        
        @functools.lru_cache
        def in_trie(i, node):
            if i == len(s):
                if node.end: self.ans = True
                return 
            c = s[i]
            if c not in node.children and c not in trie.children:
                return 
            if node.end and c not in node.children:
                in_trie(i + 1, trie.children[c])
            elif not node.end and c in node.children:
                in_trie(i + 1, node.children[c])
            elif node.end and c in node.children:
                in_trie(i + 1, node.children[c])
                in_trie(i + 1, trie.children[c])

        trie = Trie()
        for word in wordDict:
            node = trie
            for c in word:
                node = node.children[c]
            node.end = True
        
        in_trie(0, trie)
        return self.ans

    # 36 ms, 85.35%. Elegant solution from Stefan. 
    def wordBreak(self, s, words):
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]
    
    # Same as above but easier to understand. DP
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
                    
        return dp[-1]
    
    # 32 ms, 94%. Greate and easy to understand BFS, DFS solution from the dicussion
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        q = deque([s])
        seen = set() 
        while q:
            s = q.popleft()    # popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False

# @lc code=end


