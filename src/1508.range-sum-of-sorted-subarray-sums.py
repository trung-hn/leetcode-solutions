#
# @lc app=leetcode id=1508 lang=python3
#
# [1508] Range Sum of Sorted Subarray Sums
#

# @lc code=start
class Solution:
    # 476 ms, 43.22 %. Time: O(N^2logN). Space: O(N^2). There is better solution in the discussion
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for i in range(n):
            cumm = 0
            for j in range(i, n):
                cumm += nums[j]
                arr.append(cumm)
        arr.sort()
        return sum(arr[left - 1 : right]) % (10**9 + 7)
# @lc code=end

