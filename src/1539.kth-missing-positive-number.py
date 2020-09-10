#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#

# @lc code=start
# TAGS: Binary Search
class Solution:
    # 48 ms, 92.17 %. Time: O(logN). Space: O(1).
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # For edge case
        if arr[-1] - len(arr) < k:
            return arr[-1] + (k - (arr[-1] - len(arr)))
        
        lo, hi = 0, len(arr) - 1
        
        while lo < hi:
            mid = (lo + hi) // 2
            missing_no = arr[mid] - mid - 1
            if missing_no < k:
                lo = mid + 1
            else:
                hi = mid
        
        missing_no = arr[lo - 1] - lo
        return arr[lo - 1] + (k - missing_no)

    # 48 ms, 92.17 %. Time: O(logN). Space: O(1). Cleaner by using different template for Binary Search. 
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            if arr[mid] - mid - 1 < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return arr[hi] + (k - (arr[hi] - hi - 1))
            
        
# @lc code=end

