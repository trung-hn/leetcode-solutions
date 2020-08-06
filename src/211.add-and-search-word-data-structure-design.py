#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#

# @lc code=start
# TAGS: Trie, Design
class WordDictionary:
    """
    TLE
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.visited = []
        
    # O(1)
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.visited.append(word)
        
    # O(N*M)
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        dots = word.count(".")
        for w in self.visited:
            if len(w) != len(word): continue
            diff = sum(l1 != l2 for l1, l2 in zip(w, word))
            if diff <= dots: return True
        return False

class TrieNode:
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.end = False

class WordDictionary:
    """
    408 ms, 41.93%.
    """
    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        trie = self.trie
        for c in word:
            trie = trie.next[c]
        trie.end = True

    def search(self, word: str) -> bool:
        self.rv = False
        def dfs(word, trie):
            if not word:
                if trie.end:
                    self.rv = True
                return 
            if word[0] == ".":
                for nxt in trie.next.values():
                    dfs(word[1:], nxt)
            else:
                if word[0] in trie.next:
                    dfs(word[1:], trie.next[word[0]])
                return False

        dfs(word, self.trie)
        return self.rv

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

