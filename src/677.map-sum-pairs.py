#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#

# @lc code=start
# TAGS: Trie
class Trie:
    def __init__(self):
        self.val  = 0
        self.child = collections.defaultdict(Trie)
        
class MapSum:
    # 32 ms, 64.16%. Time: O(K). Space: O(K) K is the length of the key
    def __init__(self):
        self.root = Trie()
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for c in key:
            node = node.child[c]
        node.val = val
        

    def sum(self, prefix: str) -> int:
        def dfs(node):
            return sum(dfs(child) for child in node.child.values()) + node.val
        
        node = self.root
        for c in prefix:
            node = node.child[c]
        return dfs(node)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
# @lc code=end

