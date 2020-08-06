#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
# TAGS: Array
class Solution:
    # 356 ms, 97.79%. Time and Space: O(N)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        visited = set()
        for num in nums:
            if num in visited:
                ans.append(num)
            else:
                visited.add(num)
        return ans
    
    # 400 ms, 67.83 %. Time: O(N). Space: O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                ans.append(index + 1)
            else:
                nums[index] = - nums[index]
        return ans


# @lc code=end

