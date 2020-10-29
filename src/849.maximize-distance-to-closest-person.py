#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#

# @lc code=start    
# TAGS: Array
class Solution:
    # 128 ms, 82.85%. Time and Space: O(N)
    def maxDistToClosest(self, seats: List[int]) -> int:
        filled_seats = [i for i, v in enumerate(seats) if v]
        filled_seats = [-filled_seats[0]] + filled_seats + [len(seats) - 1 - filled_seats[-1] + len(seats) - 1]
        
        space = 0
        for s1, s2 in zip(filled_seats, filled_seats[1:]):
            if s1 + 1 == s2: continue
            mid = (s1 + s2) // 2
            space = max(space, mid - s1)
        return space
    
    # Time: O(N). Space: O(1). Two pointers.
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, last, N = 0, -1, len(seats)
        for i, seat in enumerate(seats):
            if seat:
                res = max(res, i if last < 0 else (i - last) // 2)
                last = i
        return max(res, (N - 1 - last))
# @lc code=end

