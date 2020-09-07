#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
# TAGS: Hash Table

import itertools
class Solution:
    # 36 ms, 66 % pythonic code using set
    def wordPattern1(self, pattern: str, str: str) -> bool:
        t = str.split()
        p = pattern
        return len(set(zip(p,t))) == len(set(p)) == len(set(t)) and len(p) == len(t)
    
    # 32 ms, 60.84 %. Time and Space: O(N)
    def wordPattern(self, pattern: str, str: str) -> bool:
        S = str.split()
        if len(S) != len(pattern): return False
        match1 = {}
        match2 = {}
        for c, word in itertools.zip_longest(pattern, S):
            if c in match1 and word in match2:
                if match1[c] != word: return False        
                if match2[word] != c: return False
            elif c not in match1 and word not in match2:
                match1[c] = word
                match2[word] = c
            else:
                return False
        return True

    # 32 ms 89 %. Time and Space: O(N)
    def wordPattern(self, pattern: str, str: str) -> bool:
        S = str.split()
        if len(S) != len(pattern) or len(set(S)) != len(set(pattern)): return False
        D = {}
        for i, c in enumerate(pattern):
            if c in D and S[i] != D[c]: return False
            D[c] = S[i]
        return True
            
# @lc code=end