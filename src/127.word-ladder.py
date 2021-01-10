#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    # 136 ms, 61.7%. Time and Space: O(M^2*N). M if word length, N is numbner of words
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff(w1, w2):
            return sum(c1 != c2 for c1, c2 in zip(w1, w2))
        
        # Make graph
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + "*" + word[i+1:]].append(word)
                    
        visited = set()
        queue = [beginWord]
        depth = 0
        while queue:
            cur = set()
            depth += 1
            for word in queue:
                visited.add(word)
                if word == endWord: return depth
                for i in range(len(word)):
                    modified_word = word[:i] + "*" + word[i+1:]
                    for nxt in graph[modified_word]:
                        if nxt in visited: continue
                        cur.add(nxt)
            queue = cur
        return 0

# @lc code=end

