#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
# TAGS: Binary Search
import bisect
class Solution:
    # 304 ms, 58.6%. Time: O(logN+KlogK). Space:O(K)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect.bisect_left(arr, x)
        cnt = 0; ans = []
        lo = index - 1; hi = index 
        while cnt < k:
            if lo < 0 or hi < len(arr) and x - arr[lo] > arr[hi] - x:
                ans.append(arr[hi])
                hi += 1
            elif hi == len(arr) or x - arr[lo] <= arr[hi] - x:
                ans.append(arr[lo])
                lo -= 1  
            cnt += 1
        return sorted(ans)
    
    # 284 ms, 82.11%. Time: O(logN+logK). Space:O(K)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        index = bisect.bisect_left(arr, x)
        lo = index - 1; hi = index; cnt = 0
        while 0 <= lo < hi < len(arr) and cnt < k:
            if x - arr[lo] > arr[hi] - x:
                hi += 1
            elif x - arr[lo] <= arr[hi] - x:
                lo -= 1  
            cnt += 1
        if lo == -1: return arr[:k]
        if hi == len(arr): return arr[-k:]        
        return arr[lo + 1:hi]
    
    # 312 ms, 48.80%. Time: O(NlogN). Space: O(N) Custom sort
    def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
        def custom_key(val):
            return abs(val - x)
        arr.sort(key=custom_key)
        return sorted(arr[:k]) 
# @lc code=end

