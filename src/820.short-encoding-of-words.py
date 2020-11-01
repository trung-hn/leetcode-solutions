#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#

# @lc code=start
# TAGS: Trie
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.end = True
class Solution:
    # 260 ms, 20.48%. Time and Space: O(M*N)
    def minimumLengthEncoding(self, words: List[str]) -> int:
        flipped = [word[::-1] for word in words]

        root = Trie()
        for word in flipped:
            node = root
            for c in word:
                node = node.children[c]
            node.end = True
        
        def dfs(node, depth=1):
            if node.end and not node.children:
                return depth
            rv = 0
            for child in node.children.values():
                rv += dfs(child, depth + 1)
            return rv
        return dfs(root)
    
    # 112 ms, 86.75%. Same complexity but simpler
    def minimumLengthEncoding(self, words):
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return sum(len(w) + 1 for w in s)
# @lc code=end

