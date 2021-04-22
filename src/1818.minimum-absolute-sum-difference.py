#
# @lc app=leetcode id=1818 lang=python3
#
# [1818] Minimum Absolute Sum Difference
#

# @lc code=start
# TAGS: Binary Search, Greedy


class Solution:
    """
    Approach:
    Sort nums1 and perform binary search on it to find best gain
    """
    # 91.99%. Time: O(NlogN). Space: O(sort)

    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:

        # bisect right
        def binary_search(nums, target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        nums = sorted(nums1)
        total = gain = 0
        for n1, n2 in zip(nums1, nums2):
            total += abs(n1 - n2)
            index = binary_search(nums, n2)

            # Get most change
            if index:
                gain = max(gain, abs(n1 - n2) - abs(nums[index - 1] - n2))
            if index < len(nums):
                gain = max(gain, abs(n1 - n2) - abs(nums[index] - n2))
        return (total - gain) % (10**9 + 7)

# @lc code=end
