#
# @lc app=leetcode id=1797 lang=python3
#
# [1797] Design Authentication Manager
#

# @lc code=start
# TAGS: Hash Table, Design


class AuthenticationManager:
    """
    132 ms, 94.83%.
    Time: O(Design). Space: O(N)
    """

    def __init__(self, timeToLive: int):
        self.expire_time = {}
        self.queue = collections.deque()
        self.lifespan = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.checkExpired(currentTime)
        # Update expire_time and add it queue
        self.expire_time[tokenId] = currentTime + self.lifespan
        self.queue.append((self.expire_time[tokenId], tokenId))

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.checkExpired(currentTime)
        if tokenId in self.expire_time:
            # Update expire_time and add it queue
            self.expire_time[tokenId] = currentTime + self.lifespan
            self.queue.append((self.expire_time[tokenId], tokenId))

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.checkExpired(currentTime)
        return len(self.expire_time)

    # Clean up queue and expire_time. TIme: O(N)
    def checkExpired(self, currentTime):
        # while expired time <= currentTime, pop it
        while self.queue and self.queue[0][0] <= currentTime:
            time, id_ = self.queue.popleft()
            # If expired time == latest expire_time, del
            if time == self.expire_time[id_] and self.expire_time[id_] <= currentTime:
                del self.expire_time[id_]

# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
# @lc code=end
