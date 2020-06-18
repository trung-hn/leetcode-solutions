#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
# TAGS: Array, Hash Table, Design
# REVIEWME: remove value from a list in O(1)
import random
class RandomizedSet:
    """
    Overall:
    Time: O(1)
    Space: O(N)
    The most important part about this is how to remove in value from a list in O(1)
    by swapping wanted value to the end and pop it. 
    We keep track of the position with dictionary
    """
    # 92 ms, 96.28%
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.D = {}
        self.data = []
        

    # O(1). Easy
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.D:
            self.D[val] = len(self.data)
            self.data.append(val)
            return True
        
    # O(1). Important part
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.D:
            
            self.data[self.D[val]] = self.data[-1]
            self.D[self.data[-1]] = self.D[val]
            self.data.pop()
            del self.D[val]
            return True
        
    # O(1). Easy
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

