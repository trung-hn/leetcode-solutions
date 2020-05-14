#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# TAGS: Design, Trie
# @lc code=start
class TrieNode:
    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.end = False
        
# 244 ms, 26.4%. Recursion
class Trie:
    def __init__(self):
        self.head = TrieNode()
        
    def insert(self, word: str) -> None:
        def insert_node(word, node):
            if not word: 
                node.end = True
                return
            char = word[0]
            if char not in node.next: node.next[char] = TrieNode()
            insert_node(word[1:], node.next[char])
        insert_node(word, self.head)

    def search(self, word: str) -> bool:
        def search_node(word, node):
            if not word:
                return node.end
            char = word[0]
            if char not in node.next: return False
            return search_node(word[1:], node.next[char])
        return search_node(word, self.head)

    def startsWith(self, prefix: str) -> bool:
        def starts_with_node(prefix, node):
            if not prefix:
                return True
            char = prefix[0]
            if char not in node.next: return False
            return starts_with_node(prefix[1:], node.next[char])
        return starts_with_node(prefix, self.head)


# 180 ms, 72.91%. Iteration
class Trie:
    # O(1), O(1)
    def __init__(self):
        self.head = TrieNode()
    
    # O(m), O(m)
    def insert(self, word: str) -> None:
        node = self.head
        for char in word:
            node = node.next[char]
        node.end = True

    # O(m), O(1)
    def search(self, word: str) -> bool:
        node = self.head
        for char in word:
            if char not in node.next: return False
            node = node.next[char]
        return node.end
    
    # O(m), O(1)
    def startsWith(self, word: str) -> bool:
        node = self.head
        for char in word:
            if char not in node.next: return False
            node = node.next[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

