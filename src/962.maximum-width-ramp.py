#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
# TAGS: Array
# REVIEWME: Array
class Solution:
    # 452 ms, 15.49%. Time: O(NlogN). Space: O(N)
    def maxWidthRamp(self, A: List[int]) -> int:
        
        def binary_search(target, nums):
            left, right = 0, len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        ans = 0
        indices = []; stack = []
        for i, num in enumerate(A):     
            if stack and stack[-1] <= num:
                index = binary_search(num, stack)
                ans = max(ans, i - indices[index])
            if not stack or stack[-1] > num:
                stack.append(num)
                indices.append(i)
        return ans
# @lc code=end

