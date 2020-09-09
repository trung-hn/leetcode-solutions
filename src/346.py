"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""
# TAGS: Design, Array
class MovingAverage:
    # 60 ms, 92%. Time: O(1). Space: O(N)
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.store = []
        self.size = size
        self.p = -1
        self.total = 0

    def next(self, val: int) -> float:
        
        self.p = (self.p + 1) % self.size
        if self.size > len(self.store):
            self.store.append(val)
        else:
            self.total -= self.store[self.p]
            self.store[self.p] = val
            
        self.total += val
        return self.total / len(self.store)

class MovingAverage:
    # Same Complexity but not as clean solution. 
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.num = [0] * size
        self.index = 0
        self.full = False
        self.total = 0

    def next(self, val: int) -> float:
        self.total += val
        
        if self.full:
            self.total -= self.num[self.index]
        
        self.num[self.index] = val
        self.index += 1
        
        if self.index == len(self.num):
            self.full = True
        
        self.index %= len(self.num)
        
        if self.full:
            return self.total / len(self.num)
        return self.total / self.index


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)