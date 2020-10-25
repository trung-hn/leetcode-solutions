# TAGS: Premium, DFS, Union Find

class Solution:
    # From article. Worse complexity than the one below. 
    # The idea is to create a graph and DFS on it.
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        if len(words1) != len(words2): return False
        graph = collections.defaultdict(list)
        for w1, w2 in pairs:
            graph[w1].append(w2)
            graph[w2].append(w1)

        for w1, w2 in zip(words1, words2):
            stack, seen = [w1], {w1}
            while stack:
                word = stack.pop()
                if word == w2: break
                for nei in graph[word]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            else:
                return False
        return True

    # 468 ms, 80.35%. Time: o(NP).Space: O(N). Time complexity is quite complicated but o(NP) would be loose upper bound
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        class UF:
            def __init__(self):
                self.parent = {}
            
            def union(self, parent, child):
                self.parent[self.find(child)] = self.find(parent)
            
            def find(self, x):
                if x not in self.parent:
                    self.parent[x] = x
                elif self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
        if len(words1) != len(words2):
            return False
        
        union = UF()
        for p, c in pairs:
            union.union(p, c)
        
        for w1, w2 in zip(words1, words2):
            if union.find(w1) != union.find(w2):
                return False
        return True
                