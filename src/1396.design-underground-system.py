#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
# TAGS: Design


class UndergroundSystem:
    # 232 ms,89.4%. Time and Space: O(N)
    def __init__(self):
        self.on_board = {}
        self.records = collections.defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.on_board[id] = (stationName, t)

    def checkOut(self, id: int, off_station: str, t: int) -> None:
        on_station, on_time = self.on_board.pop(id)
        key = (on_station, off_station)
        self.records[key][0] += t - on_time
        self.records[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.records[key][0] / self.records[key][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end
