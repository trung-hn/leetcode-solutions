#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#

# @lc code=start
# TAGS: Array, Math


class Solution:
    """
    Approach:
    Track when customer get on or off then cummulate the values
    """
    # 832 ms, 91.73 %. Time and Space: O(N)

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # Track when customer get on or off
        tracker = [0] * (n + 1)
        for s, e, seat in bookings:
            tracker[s - 1] += seat
            tracker[e] -= seat

        # Calculate customer at each time on the flight
        for i in range(1, n):
            tracker[i] += tracker[i - 1]
        return tracker[:-1]
# @lc code=end
