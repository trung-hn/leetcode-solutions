#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
# TAGS: Dynamic Programming
class Solution:
    # 196 ms, 86.88%. Time and Space: O(M*N). M is target, N is len(nums). 
    # It is O(M*N) because there are N num and there are only M possibal values for sofar
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        
        @functools.lru_cache(None)
        def dfs(i=0, sofar=0):
            if i == len(nums) or sofar > target: return False
            if sofar == target: return True
            return dfs(i + 1, sofar + nums[i]) or dfs(i + 1, sofar)
        return dfs()
    
    # From discussion. DP TIme: O(M*N). Space: O(M)
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 == 1: return False
            
        target = total / 2   #target sum 
        s = set([0])         #stores the sums of the subsets    
        for n in nums:
            sums_with_n = []  #stores the sums of the subsets that contain n
            for i in s:
                if i + n == target: return True
                if i + n < target:
                    sums_with_n.append(i + n)
            s.update(sums_with_n)
        return False

# @lc code=end

