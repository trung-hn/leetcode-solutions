#
# @lc app=leetcode id=1845 lang=python3
#
# [1845] Seat Reservation Manager
#

# @lc code=start
# TAGS: Heap, Design


class SeatManager:
    """
    592 ms, 68.55%.
    Time: O(logN). Space: O(N)
    """

    def __init__(self, n: int):
        self.heap = list(range(1, n + 1))
        heapq.heapify(self.heap)

    def reserve(self) -> int:
        return heapq.heappop(self.heap)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heap, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# @lc code=end
