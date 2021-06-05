#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
# TAGS: Array


class Solution:
    # 36 ms, 94.11%. Time: O(N^2). Space: O(N)
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix_sum = [0]
        for val in arr:
            prefix_sum.append(prefix_sum[-1] + val)

        total = 0
        for i in range(len(prefix_sum)):
            for j in range(i + 1, len(prefix_sum), 2):
                total += prefix_sum[j] - prefix_sum[i]
        return total

    # 28 ms, 99.2%. Time: O(N). Space: O(1).
    # at index 0, there is 1 way to start and N ways to end
    # at index 1, there are 2 ways to start and N - 1 ways to end.
    # at index i, there are (i + 1) ways to start and (N - i) ways to end
    # => (i + 1) * (N - i) ways to make subarray (even and odd length)
    # => There are ((i + 1) * (N - i) + 1) // 2 odd len sub-array
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        N = len(arr)
        for i, num in enumerate(arr):
            total += ((i + 1) * (N - i) + 1) // 2 * num
        return total


# @lc code=end
"""
1 4 2 5 3
1 5 7 12 15

1 2 3
2 2 2

1 2 3 4
2 3 3 2

1 4 2 5 3
3 4 5 4 3

1 2 3 4 5 6 
3 5 6 6 5 3

1 2 3 4 5 6 7
"""
