# TAGS: Premium, Back Tracking, Trie
# REVIEWME: Back Tracking, Trie, Hard
import collections
class Solution:
    """
    Need to look at solution article to write the first solution. 
    """

    # 400 ms, 68.03%. Time: O(N*26^L*L). Space: O(N*L+N*L/2)
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.ans = []
        self.length = len(words[0])
        
        self.build_prefix_hashtable(words)
        for word in words:
            self.square = [word]
            self.back_track()
        return self.ans

    def back_track(self, step=1):
        if step == self.length:
            self.ans.append(self.square[:])
            return 
        
        prefix = "".join(word[step] for word in self.square)
        for word in self.get_words_with_prefix(prefix):
            self.square.append(word)
            self.back_track(step + 1)
            self.square.pop()

    def build_prefix_hashtable(self, words):
        self.prefix_hashtable = collections.defaultdict(set)
        for word in words:
            for prefix in (word[:i] for i in range(len(word))):
                self.prefix_hashtable[prefix].add(word)

    def get_words_with_prefix(self, prefix):
        return self.prefix_hashtable[prefix]


class Solution:
    """Trie solution"""
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        self.words = words
        self.N = len(words[0])
        self.buildTrie(self.words)

        results = []
        word_squares = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def buildTrie(self, words):
        self.trie = {}

        for wordIndex, word in enumerate(words):
            node = self.trie
            for char in word:
                if char in node:
                    node = node[char]
                else:
                    newNode = {}
                    newNode['#'] = []
                    node[char] = newNode
                    node = newNode
                node['#'].append(wordIndex)

    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return [self.words[wordIndex] for wordIndex in node['#']]