#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
# TAGS: Array, Backtracking
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        lst = []
        def backtracking(nums, target, index=0, sofar=0, path=[]):
            for i in range(index, len(nums)): 
                num = nums[i]
                if sofar + num == target:
                    lst.append(path + [num])
                    return 
                elif sofar + num < target:
                    backtracking(candidates, target, i, sofar + num, path + [num])
                else: return
                  
        backtracking(candidates, target)
        return lst
    
    # 76 ms, 70%. Second solution. Time: O(N^2). Space: O(N)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def dfs(nums, target, index=0, sofar=[]):
            if target < 0: return
            if target == 0:
                self.ans.append(sofar)
                return 
            for i in range(index, len(nums)):
                dfs(nums, target - nums[i], i, sofar + [nums[i]])
        dfs(candidates, target)
        return self.ans
# @lc code=end

