#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
# TAGS: Design
class MyHashSet:
    # 164 ms, 80%.
    # O(1)
    def __init__(self):
        self.size = 1000
        self.store = [[] for _ in range(self.size)]
        
    # O(N)
    def add(self, key: int) -> None:
        k = self.hash_n(key)
        if key not in self.store[k]:
            self.store[k].append(key)
    
    # O(N)
    def remove(self, key: int) -> None:
        k = self.hash_n(key)
        if key in self.store[k]:
            self.store[k].remove(key)

    # O(N)
    def contains(self, key: int) -> bool:
        k = self.hash_n(key)
        return key in self.store[k]
        
    # O(1)
    def hash_n(self, key:int):
        return key % self.size

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

