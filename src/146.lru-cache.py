#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
# TAGS: Hash Table, Linked List, Design, Doubly-Linked List
import heapq


# Using Heap and Doubly Linked-List
class Node:
    def __init__(self, key, val, nxt=None, prev=None):
        self.val = val
        self.next = nxt
        self.prev = prev
        self.key = key


class LRUCache:
    # 224 ms, 40%.
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        # Linked list
        self.tail = Node(None, None)
        self.head = Node(None, None, self.tail)
        self.tail.prev = self.head  # head - tail

    # O(1)
    def get(self, key: int) -> int:
        # will not remove anything, only update timestamp.
        if key not in self.cache:
            return -1
        self.update_order(key, self.cache[key].val)
        return self.cache[key].val

    # O(1)
    def put(self, key: int, val: int) -> None:
        if len(self.cache) == self.cap:
            if key not in self.cache:
                # head <-> 1 <-> tail
                # head <-> tail
                cur = self.head.next
                del self.cache[cur.key]
                cur.prev.next = cur.next
                cur.next.prev = cur.prev

        self.update_order(key, val)

    def update_order(self, key, val):
        if key in self.cache:
            # head - 2 - 1 - tail, want to remove key 2
            cur = self.cache[key]  # head -> 1 <-> tail, 2
            cur.prev.next = cur.next  # head -> 1 <-> tail
            cur.next.prev = cur.prev  # head <-> 1 <-> tail

        self.put_to_tail(key, val)
        self.cache[key] = self.tail.prev

    def put_to_tail(
        self, key, val
    ):  #  head - 2 - tail  => head - 2 - 1 - tail aftering putting 1
        cur = Node(key, val, self.tail, self.tail.prev)  # head <-> 2 <- 1 -> tail
        cur.prev.next = cur  # head <-> 2 <-> 1 -> tail
        self.tail.prev = cur  # head <-> 2 <-> 1 <-> tail


# Using Heap and Dict
class LRUCache:
    def __init__(self, capacity: int):
        self.timer = 0
        self.heap = []
        self.cache = {}
        self.capacity = capacity

    def update_lru(self, key, value):
        heapq.heappush(self.heap, (self.timer, key))
        self.cache[key] = [self.timer, value]
        self.timer += 1
        while len(self.cache) > self.capacity:
            ts, key = heapq.heappop(self.heap)
            if self.cache[key][0] == ts:
                del self.cache[key]

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key][1]
            self.update_lru(key, val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        self.update_lru(key, value)


# @lc code=end
