#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
# TAGS: Queue
import bisect, collections
class RecentCounter:

    def __init__(self):
        self.pings = []
        self.pings2 = collections.deque()
    
    # 284 ms, 97.70%. Binary Search. O(log(N))
    def ping(self, t: int) -> int:
        self.pings.append(t)
        index = bisect.bisect_left(self.pings, t - 3000)
        return len(self.pings) - index

    # 268 ms, 99.98%. Time and Space: O(3000) = O(1)
    def ping(self, t: int) -> int:
        self.pings2.append(t)
        while self.pings2[0] < t - 3000:
            self.pings2.popleft()
        return len(self.pings2)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

