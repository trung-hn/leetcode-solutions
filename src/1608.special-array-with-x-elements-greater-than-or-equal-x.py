#
# @lc app=leetcode id=1608 lang=python3
#
# [1608] Special Array With X Elements Greater Than or Equal X
#

# @lc code=start
# TAGS: Binary Search, Array
class Solution:
    # 40 ms, 58.41%. Time: O(M). Space: O(N). where M in the max of nums
    def specialArray(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        total = 0
        for i in range(1001):
            if i == len(nums) - total:
                return i
            total += counter[i]
        return -1
    
    # 28 ms, 97.31%. Time: O(logN). Space: O(N)
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        for i in range(1001):
            index = bisect.bisect_left(nums, i)
            if i== len(nums) - index:
                return i
        return -1
    
    # 32 ms, 90.96%. Time: O(logN*logN). Space: O(1)
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        lo, hi = 0, nums[-1]
        while lo - 1 < hi:
            mid = (lo + hi) // 2
            index = bisect.bisect_left(nums, mid)
            greater = len(nums) - index
            
            if greater == mid: return mid
            elif greater > mid: lo = mid + 1
            else: hi = mid - 1
        return -1
        
# @lc code=end

