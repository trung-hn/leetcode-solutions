#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
# TAGS: Array, Math, Bit Manipulation
# REVIEWME: Array, Math, Bit Manipulation


class Solution:
    """
    Approach:
    1. Math: sum from 1 to N using math and find the left over
    2. Array Manipulation: flip value at index
    3. Bit Manipulation (Article): Use XOR to cancel out value and index
    """
    # 128 ms, 71.62%. Time: O(N). Space: O(1). Math

    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) + 1
        total = length * (length - 1)/2
        return int(total - sum(nums))

    # 148 ms, 20.12%. Time: O(N). Space: O(1). Array Manipulation

    def missingNumber(self, nums: List[int]) -> int:
        for num in nums:
            pos = num if num >= 0 else ~num

            # Skip edge case
            if pos == len(nums):
                continue

            # 2's complement
            nums[pos] = ~nums[pos]

        # If a num >= 0, we miss the index
        for i, num in enumerate(nums):
            if num >= 0:
                return i

        return len(nums)

    # Bit Manipulation
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
# @lc code=end
