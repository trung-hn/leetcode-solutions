#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
# TAGS: Tree
# REVIEWME: Tree
class MyCalendar:
    """
    648 ms, 34.15%. Time and Space: O(N)
    """
    def __init__(self):
        self.bookings = []        

    def book(self, start: int, end: int) -> bool:
        for start0, end0 in self.bookings:
            if end > start0 and start < end0 :
                return False
        self.bookings.append((start, end))
        return True
    
class MyCalendar:
    """
    235 ms, 88.03%. Time and Space: O(N)
    """
    def __init__(self):
        self.bookings = []        
        
    def book(self, start: int, end: int) -> bool:
        def binary_search(target, array):
            lo, hi = 0, len(array)
            while lo < hi:
                mid = (lo + hi) // 2
                if array[mid][0] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        index = binary_search(start, self.bookings)
        if self.bookings:
            # only check if not the last index
            if index < len(self.bookings) \
                and self.bookings[index][0] < end \
                and start < self.bookings[index][1]:
                return False
            # only check if not the first index
            if index > 0 \
                and self.bookings[index - 1][0] < end \
                and start < self.bookings[index - 1][1]:
                return False
        self.bookings.insert(index, [start, end])
        return True


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if not node: return

        if node.start >= self.end:
            if self.right is None:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if self.left is None:
                self.left = node
                return True
            return self.left.insert(node)
        return False

class MyCalendar:
    """
    268 ms, 77.77%. Using Tree to make search and inserting O(logN). Time: O(NlogN) Space:O(N)
    However, because this is not a balanced tree, worst case can be O(N^2)
    """
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

