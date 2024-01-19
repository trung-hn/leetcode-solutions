#
# @lc app=leetcode id=3005 lang=python3
#
# [3005] Count Elements With Maximum Frequency
#

# @lc code=start
# TAGS: Array, Hash Table, Counting
from collections import defaultdict

class Solution:
    # Time and Space: O(N)
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_cnt = 0
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
            max_cnt = max(max_cnt, counter[num])
        return sum(v for k, v in counter.items() if v == max_cnt)
# @lc code=end

