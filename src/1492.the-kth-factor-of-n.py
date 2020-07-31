#
# @lc app=leetcode id=1492 lang=python3
#
# [1492] The kth Factor of n
#

# @lc code=start
# TAGS: Math, Tricky
class Solution:
    # 36 ms, 67.31%. Time: O(NlogN) because of sorting. Space: O(N)
    def kthFactor(self, n: int, k: int) -> int:
        nums = set()
        cnt = 0
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                nums.add(i)
                nums.add(n // i)
        nums = sorted(nums)
        return -1 if k > len(nums) else nums[k - 1]

    # Time: O(logN). Space: O(logN). Very tricky with edge cases
    def kthFactor(self, n: int, k: int) -> int:
        nums = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                nums.append(i)
                k -= 1
            if not k : return i
        if nums[-1] ** 2 == n: nums.pop()
        if k > len(nums): return -1
        return n // nums[-k]

# @lc code=end

