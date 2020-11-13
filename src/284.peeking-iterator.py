#
# @lc app=leetcode id=284 lang=python3
#
# [284] Peeking Iterator
#

# @lc code=start
# TAGS: Design
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    # 32 ms, 62.88%. Time and Space: O(1)
    def __init__(self, iterator):
        self.root = iterator
        self.peeked = False
        self.peek_val = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked:
            return self.peek_val
        self.peeked = True
        self.peek_val = self.root.next()
        return self.peek_val
        

    def next(self):
        if self.peeked:
            self.peeked = False
            return self.peek_val
        return self.root.next()
        

    def hasNext(self):
        return self.peeked or self.root.hasNext()
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
# @lc code=end

