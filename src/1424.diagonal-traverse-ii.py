#
# @lc app=leetcode id=1424 lang=python3
#
# [1424] Diagonal Traverse II
#

# @lc code=start
class Solution:
    # LTE. Time and Space: O(R*C)
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        R = len(nums)
        C = max(len(row) for row in nums)
        start = [(i, 0) for i in range(R)] + [(R - 1, j) for j in range(1, C)]
        for r, c in start:
            x, y = r, c
            while x >= 0:
                if y < len(nums[x]):
                    ans.append(nums[x][y]) 
                x -= 1
                y += 1
        return ans
    
    # 1012 ms, 33.92%. Time and Space: O(A) where A is the number of numbers
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                pos = r + c
                if pos >= len(ans):
                    ans.append([])
                ans[pos].append(nums[r][c])
        return [val for row in ans for val in reversed(row)]
                
# @lc code=end

