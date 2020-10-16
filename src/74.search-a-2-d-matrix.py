#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
# TAGS: Binary Search
class Solution:
    # 44 ms, 92.85%. Time: O(logN + logM). Space: O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        def binary_search(nums, target):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if target < nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            if target >= nums[lo]:
                return lo
            return lo - 1
        
        r = binary_search([row[0] for row in matrix], target)
        c = binary_search(matrix[r], target)
        return matrix[r][c] == target
            
# @lc code=end

