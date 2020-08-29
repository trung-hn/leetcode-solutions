#
# @lc app=leetcode id=1552 lang=python3
#
# [1552] Magnetic Force Between Two Balls
#

# @lc code=start
# TAGS: Binary Search
# REVIEWME: Very Tricky problem, Template for Binary Search
class Solution:
    """
    Template for Binary Search:
    bisect_left:
        mid = (lo + hi) // 2
        if f(mid) > target:
            lo = mid + 1
        else:
            hi = mid
    Explain: we move `hi` to a known satisfied `mid` value

    bisect_right:
        mid = hi - (hi - lo) // 2
        if f(mid) >= target:
            lo = mid
        else:
            hi = mid + 1
    Explain: we move `lo` to a known satisfied `mid` value

    """
    # Inspired from https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/794070/Python-Binary-search-solution-with-explanation-and-similar-questions
    # Time: O(NlogN). Space: O(1). This is usually used for bisect_left
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def count(d):
            prev = position[0]
            cnt = 1
            for val in position[1:]:
                if val - prev >= d: 
                    cnt += 1 
                    prev = val
            return cnt
        
        lo, hi = 0, position[-1] - position[0]
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= m: # means balls are too tightly packed. we can increase space between them
                lo = mid + 1
            else: # means space are too large, we should decrease packing space. 
                hi = mid
        if count(lo) == m:
            return lo
        return lo - 1

    # 1308 ms, 87.47 %. Similar to bisect_right
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def count(d):
            prev = position[0]
            cnt = 1
            for val in position[1:]:
                if val - prev >= d: 
                    cnt += 1 
                    prev = val
            return cnt
        
        lo, hi = 0, position[-1] - position[0]
        while lo < hi:
            mid = hi - (hi - lo) // 2
            if count(mid) >= m: 
                lo = mid
            else:
                hi = mid - 1
        return lo
    
# @lc code=end
