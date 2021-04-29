#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
# TAGS: Array, Binary Search
# REVIEW: Binary Search, Template for Binary Search


class Solution:
    """
    Template for Binary Search:
    bisect_left:
        lo, hi = 0, len(nums) - 1
        mid = lo + (hi - lo) // 2
        if f(mid) > target:
            lo = mid + 1
        else:
            hi = mid
    Explain: we move `hi` to a known satisfied `mid` value

    bisect_right:
        lo, hi = 0, len(nums) - 1
        mid = hi - (hi - lo) // 2
        if f(mid) >= target:
            lo = mid
        else:
            hi = mid + 1
    Explain: we move `lo` to a known satisfied `mid` value

    """
    # 72 ms, 99.35%.

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def bi_left(target):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo if lo < len(nums) and nums[lo] == target else -1

        def bi_right(target):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                mid = hi - (hi - lo) // 2
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid
            return lo if lo < len(nums) and nums[lo] == target else -1

        left, right = bi_left(target), bi_right(target)
        return (left, right) if left <= right else [-1, -1]

    # 76 ms, 96.58%. Time: O(logN). Space: O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)
        if left == right:
            return -1, -1
        if nums[left] == nums[right - 1] == target:
            return left, right - 1
# @lc code=end
