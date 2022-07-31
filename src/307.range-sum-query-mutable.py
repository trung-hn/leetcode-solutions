#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#

# @lc code=start
# TAGS: Array, Design, Binary Indexed Tree, Segment Tree
# REVIEWME: Binary Indexed Tree
from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        deg = 0
        while 2 ** deg < len(nums):
            deg += 1
        deg += 1

        self.nums = [0] * (2 ** deg)
        self.length = 2 ** (deg - 1)

        for i in range(len(nums)):
            self.nums[i + self.length] = nums[i]

        for i in reversed(range(self.length)):
            self.nums[i] += self.nums[i * 2] + self.nums[i * 2 + 1]

    def update(self, index: int, val: int) -> None:
        # Iteratively update sum of range from leaves to root
        diff = val - self.nums[self.length + index]
        index += self.length
        while index:
            self.nums[index] += diff
            index //= 2

    def sumRange(self, left: int, right: int) -> int:
        left += self.length
        right += self.length
        total = 0
        while left <= right:
            if left % 2 == 1:
                # If it is half right, sum that individual and move to right branch
                # Notice that `left` will // 2 later
                total += self.nums[left]
                left += 1
            if right % 2 == 0:
                # If it is half left, sum that individual and move to left branch
                # Notice that `right` will // 2 later
                total += self.nums[right]
                right -= 1
            left //= 2
            right //= 2
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end
