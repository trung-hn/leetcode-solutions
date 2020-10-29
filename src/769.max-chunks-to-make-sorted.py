#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#

# @lc code=start
# TAGS: Array
import itertools
class Solution:
    # 32 ms 47.68%. Time: O(N). Space: O(1)
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = left = i = 0
        while i < len(arr):
            curr = arr[i]
            left = max(left, curr)
            if i == left:
                chunks += 1
            i += 1
        return chunks
    # 28 ms, 80.48%. Time: O(N). Space: O(1) because accumulate return an iterator
    def maxChunksToSorted(self, arr: List[int]) -> int:
        return sum(i == v for i, v in enumerate(itertools.accumulate(arr, max)))
# @lc code=end

