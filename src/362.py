# TAGS: Premium, Design
import collections
class HitCounter:
    """
    32 ms, 64.57%. Time: O(1). Space: O(N)
    """
    def __init__(self):
        self.deque = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.deque.append(timestamp)        

    def getHits(self, timestamp: int) -> int:
        while self.deque and self.deque[0] + 300 <= timestamp:
            self.deque.popleft()
        return len(self.deque)

class HitCounter:
    """
    scalable when number of hits per second could be very large
    """
    def __init__(self):
        self.data = [[0, i + 1] for i in range(300)]

    def hit(self, timestamp: int) -> None:
        idx = (timestamp - 1) % 300
        if self.data[idx][1] == timestamp:
            self.data[idx][0] += 1
        else:
            self.data[idx][0] = 1
            self.data[idx][1] = timestamp

    def getHits(self, timestamp: int) -> int:
        ans = 0
        for freq, val in self.data:
            if val + 300 > timestamp:
                ans += freq
        return ans

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)