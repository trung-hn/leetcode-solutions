#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
# TAGS: Array, Two Pointers
class Solution:
    # Pointers from the middle
    def sortedSquares(self, nums: List[int]) -> List[int]:
        close_to_zero = float("inf"); pos = 0
        for i, num in enumerate(nums):
            if abs(num) < close_to_zero:
                close_to_zero = abs(num)
                pos = i
        ans = [nums[pos]**2]
        left = pos - 1
        right = pos + 1
        while left >=0 or right < len(nums):
            if left < 0:
                ans.append(nums[right] ** 2)
                right += 1
            elif right >= len(nums):
                ans.append(nums[left] ** 2)
                left -= 1
            elif abs(nums[left]) > abs(nums[right]):
                ans.append(nums[right] ** 2)
                right += 1
            else:
                ans.append(nums[left] ** 2)
                left -= 1
        return ans
    
    # 252 ms, 23.52%. Time: O(N). Space: O(N) Pointers from 2 sides
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        left = 0; right = len(nums) - 1
        while left <= right:
            val1 = nums[left] ** 2
            val2 = nums[right] ** 2
            if val1 > val2:
                ans.append(val1)
                left += 1
            else:
                ans.append(val2)
                right -= 1
        return reversed(ans)
    

# @lc code=end

