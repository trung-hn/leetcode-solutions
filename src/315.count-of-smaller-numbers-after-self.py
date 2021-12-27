#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
# TAGS: Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Ser
# REVIEWME: Merge Sort
class Solution:
    # Time: O(NlogN). Space: O(N)
    def countSmaller(self, nums: List[int]) -> List[int]:

        def merge_sort(indexes):
            half = len(indexes) // 2
            if half:
                left, right = merge_sort(
                    indexes[:half]), merge_sort(indexes[half:])
                for i in reversed(range(len(indexes))):
                    if not right or left and nums[left[-1]] > nums[right[-1]]:
                        counter[left[-1]] += len(right)
                        indexes[i] = left.pop()
                    else:
                        indexes[i] = right.pop()
            return indexes

        counter = [0] * len(nums)
        merge_sort(list(range(len(nums))))
        return counter
# @lc code=end
