#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#

# @lc code=start
# TAGS: Dynamic Programming
# REVIEWME: Dynamic Programming
class Solution:
    # 1056 ms, 30.59%. Time: O(N^2). Space: O(N). Recursion with memo
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
    
        @functools.lru_cache(None)
        def dfs(i):
            rv = max_rv = cnt = 0
            curr_cnt = 1
            val = nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] > val:
                    rv, cnt = dfs(j)
                    if rv > max_rv:
                        max_rv = rv
                        curr_cnt = cnt
                    elif rv == max_rv:
                        curr_cnt += cnt
            return max_rv + 1, curr_cnt
        
        arr = []
        for i in range(len(nums)):
            arr.append(dfs(i))
        max_val = max(val for val, cnt in arr)
        return sum(cnt for val, cnt in arr if val == max_val)
    
    # 1252 ms, 19.73%. Time: O(N^2). Space: O(N). DP
    def findNumberOfLIS1(self, nums: List[int]) -> int:
        if not nums: return 0
        arr = [[1, 1]]
        for i in range(1, len(nums)):
            path_cnt = 1
            longest_path = 0
            for j, (path, cnt) in enumerate(arr):
                if nums[j] < nums[i]:
                    if path > longest_path:
                        longest_path = path
                        path_cnt = cnt
                    elif path == longest_path:
                        path_cnt += cnt
            arr.append([longest_path + 1, path_cnt])
        
        max_val = max(val for val, cnt in arr)
        return sum(cnt for val, cnt in arr if val == max_val)

    # 1028 ms, 32.09%. Time: O(N^2). Space: O(N). Same as above but cleaner
    def findNumberOfLIS1(self, nums: List[int]) -> int:
        if not nums: return 0
        lengths = [0] * len(nums)
        counts = [0] * len(nums)
        for i in range(1, len(nums)):
            for j, (path, cnt) in enumerate(arr):
                if nums[j] < nums[i]:
                    if lengths[i] > lengths[j]:
                        lengths[i] = lengths[j]
                        counts[j] = counts[i] + 1
                    elif lengths[i] == lengths[j]:
                        counts[j] += counts[i]
        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)
                
                 
# @lc code=end

