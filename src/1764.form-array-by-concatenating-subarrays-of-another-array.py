#
# @lc app=leetcode id=1764 lang=python3
#
# [1764] Form Array by Concatenating Subarrays of Another Array
#

# @lc code=start
# TAGS: Array, Greedy
# REVIEWME: Array, Greedy, KMP, New Algorithm


class Solution:
    # 84 ms, Time: O(N*M). Space: O(1)
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        start = 0
        for group in groups:
            for i in range(start, len(nums)):
                if group == nums[i: i + len(group)]:
                    start = i + len(group)
                    break
            else:
                return False
        return True

    # 64 ms, Time: O(N+M). Space: O(M). KMP algorithm
    # Explanation: https://www.youtube.com/watch?v=V5-7GzOfADQ
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        start = 0
        for group in groups:
            failure = [0] * len(group)
            # Create failure array
            j = 0
            for k in range(1, len(group)):
                while j > 0 and group[k] != group[j]:
                    j = failure[j - 1]
                j += group[k] == group[j]
                failure[k] = j

            # seach subarray in array
            j = 0
            for k in range(start, len(nums)):
                while j > 0 and nums[k] != group[j]:
                    j = failure[j - 1]
                j += nums[k] == group[j]
                if j == len(group):
                    start = k + 1
                    break
            else:
                return False
        return True
# @lc code=end
