#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
# TAGS: Array, Binary Search
class Solution:
    # 2248 ms, 39.56%. Binary Search, Time: O(NlogN). Space: O(N)
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1 

        def generate_sequence(t): # return the bloom status at after time t
            return [val <= t for val in bloomDay]

        def is_ready(status, k, m): # check if the sequence is ready
            cnt = curr = 0
            for val in status:
                if val == True:
                    curr += 1
                else:
                    curr = 0
                if curr == k:
                    cnt += 1
                    curr = 0
            return cnt >= m
        
        lo = min(bloomDay)
        hi = max(bloomDay)

        while lo < hi: # O(logN)
            mid = (lo + hi) // 2
            status = generate_sequence(mid) # O(N)
            ready = is_ready(status, k, m) # O(N)
            if ready: hi = mid
            else: lo = mid + 1

        return lo

    # 1824 ms, 61.65%. Improved version by doing it in 1 pass. Same complexity
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1 
        lo = min(bloomDay)
        hi = max(bloomDay)
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = curr = 0
            for val in bloomDay:
                if val <= mid:
                    curr += 1
                else:
                    curr = 0
                if curr == k :
                    cnt += 1
                    curr = 0
            ready = cnt >= m
            if ready: hi = mid
            else: lo = mid + 1

        return lo
# @lc code=end