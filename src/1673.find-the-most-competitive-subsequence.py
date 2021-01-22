#
# @lc app=leetcode id=1673 lang=python3
#
# [1673] Find the Most Competitive Subsequence
#

# @lc code=start
# TAGS: Stack, Heap, Greedy, Queue
class Solution:
    # LTE. Time: O(N*K). Space: O(K)
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        def get_min(start, end):
            min_index = start
            min_val = nums[start]
            for i in range(start, end):
                if nums[i] < min_val:
                    min_index, min_val = i, nums[i]
            return min_index, min_val
        
        ans = []
        index = -1
        for i in range(1, k + 1):
            index, val = get_min(index + 1, len(nums) - (k - i))
            ans.append(val)
        return ans
        
    # 1344 ms, 46.88%. Time: O(N). Space: O(K)
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        ans = []
        for i, num in enumerate(nums):
            if not ans or (num >= ans[-1] and len(ans) < k):
                ans.append(num)
            elif num < ans[-1]:
                while ans and num < ans[-1] and i <= N - 1 - (k - len(ans)):
                    ans.pop()
                ans.append(num)
        return ans
# @lc code=end

