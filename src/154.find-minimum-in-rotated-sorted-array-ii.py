#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
# TAGS: Binary Search
# REVIEWME:
# Post: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/644511/Python-Divide-and-Conquer.-A-different-variation-of-Binary-Search.
class Solution:
    """
    There are solutions here. I wrote the first one. The second one if from the article.
    Both has the time complexity of O(log N) and Space O(1)
    However, it would be O(N) in worst case where all numbers are the same.
    """
    # 52 ms, 74.41%. Divide and conquer
    def findMin(self, nums: List[int]) -> int:
        def binary_search(lo, hi):
            while lo < hi:
                mid = (lo + hi)//2
                val = nums[mid]
                if val < nums[hi]:
                    hi = mid
                elif val > nums[hi]:
                    lo = mid + 1
                else:
                    return min(binary_search(lo, mid), binary_search(mid+1, hi))
            return nums[lo]
        return binary_search(0, len(nums) - 1)
    
    # 52 ms, 74.41%. Binary Search
    def findMin(self, nums: List[int]) -> int:    
        low = 0
        high = len(nums)-1
        while high > low:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                high = pivot 
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1
        return nums[low]
# @lc code=end

