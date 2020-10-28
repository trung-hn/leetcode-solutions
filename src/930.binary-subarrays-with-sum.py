#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
# TAGS: Hash Table, Two Pointers
class Solution:
    # LTE. Time: O(N^2)
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        nums = list(itertools.accumulate(A, initial=0))
        ans = 0
        for i, num1 in enumerate(nums):
            for num2 in nums[i + 1:]:
                if num2 - num1 == S:
                    ans += 1
        return ans
    
    # 236 ms, 99.01%. Time and Space: O(N)
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        nums = list(itertools.accumulate(A, initial=0))
        freq = collections.defaultdict(int)
        ans = 0
        for num in nums:
            ans += freq[num - S]
            freq[num] += 1
        return ans
# @lc code=end

