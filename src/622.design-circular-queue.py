#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#

# @lc code=start
# TAGS: Design, Queue
class MyCircularQueue:
    """ 68 ms, 80.47% """
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.data = [None] * k
        self.head = self.tail = self.len = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.data[self.head] is None:
            self.data[self.head] = value
            self.head = (self.head + 1) % len(self.data)
            self.len += 1
            return True
        return False
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.len:
            self.data[self.tail] = None
            self.tail = (self.tail + 1) % len(self.data)
            self.len -= 1
            return True
        return False
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.len:
            return self.data[self.tail]
        return -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.len:
            temp = (self.head - 1) % len(self.data)
            return self.data[temp]
        return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.len == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.len == len(self.data)
    
class Node:
    def __init__(self, value, nxt=None):
        self.val = value
        self.next = nxt
        
class MyCircularQueue:
    """ 64 ms, 92.87% """
    def __init__(self, k: int):
        self.limit = k
        self.head = self.tail = Node(None)
        self.len = 0
        

    def enQueue(self, value: int) -> bool:
        if self.len < self.limit:
            if self.len == 0:
                self.head = self.tail = Node(value)
            else:
                self.head.next = Node(value)
                self.head = self.head.next
            self.len += 1
            return True
        return False
        

    def deQueue(self) -> bool:
        if self.len:
            self.tail = self.tail.next
            self.len -= 1
            return True
        return False
        

    def Front(self) -> int:
        if self.len:
            return self.tail.val
        return -1

    def Rear(self) -> int:
        if self.len:
            return self.head.val
        return -1
        

    def isEmpty(self) -> bool:
        return self.len == 0
        

    def isFull(self) -> bool:
        return self.len == self.limit
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

