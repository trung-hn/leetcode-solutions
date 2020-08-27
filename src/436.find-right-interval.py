#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
# TAGS: Binary Search
import bisect
class Solution:
    """
    This is a bad problem, Description is not clear. 
    """
    # 372 ms, 70.47%. Time: O(NlogN). Space: O(N)
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        nums = []
        for i, (a, b) in enumerate(intervals):
            nums.append((a, i))
        nums.sort()

        ans = []
        for a, b in intervals:
            lo = 0
            hi = len(intervals) - 1
            index = -1
            while lo < hi:
                mid = (lo + hi) // 2
                val, index = nums[mid]
                if b <= val:
                    hi = mid
                else:
                    lo = mid + 1
            if nums[lo][0] < b:
                ans.append(-1)
            else:
                ans.append(nums[lo][1])
        return ans

    # 296 ms, 96.11%. Similar to above but pythonic
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        nums = []
        seen = {}
        for i, (a, _) in enumerate(intervals):
            nums.append(a)
            seen[a] = i
        nums.sort()

        ans = []
        for a, b in intervals:
            index = bisect.bisect_left(nums, b)
            if index >= len(nums):
                ans.append(-1)
            else:
                ans.append(seen[nums[index]])
        return ans
        
# @lc code=end

