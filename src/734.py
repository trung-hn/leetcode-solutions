# TAGS: Premium, Hash Table
class Solution:
    # 40 ms, 92%
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        D = collections.defaultdict(set)
        for pair in pairs:
            D[pair[0]].add(pair[1])
            D[pair[1]].add(pair[0])
        
        for i in range(len(words1)):
            if words1[i] == words2[i] or words2[i] in D[words1[i]]:
                continue
            return False
        return True
    # 48 ms, 47% Pythonic
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2): return False
        S = set()
        for w1, w2 in pairs:
            S.add((w1,w2))
            S.add((w2,w1))
        
        return all(w1 == w2 or (w1, w2) in S for w1, w2 in zip(words1, words2))
    
    # 48 ms, 59.58%. Time and Space: O(N)
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False
        similarPairs = set(tuple(pair) for pair in similarPairs)
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2 or (w1, w2) in similarPairs or (w2, w1) in similarPairs:
                continue
            return False
        return True