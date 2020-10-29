#
# @lc app=leetcode id=768 lang=python3
#
# [768] Max Chunks To Make Sorted II
#

# @lc code=start
# TAGS: Array
# REVIEWME: Array
class Solution:
    # 88 ms, 37.4%. Time: O(NlogN). Space: O(N)
    def maxChunksToSorted(self, arr: List[int]) -> int:
        nums = []
        counter = collections.Counter()
        for val in arr:
            counter[val] += 1
            nums.append((val, counter[val]))
            
        nums2 = itertools.accumulate(nums, max)
        return sum(v1 == v2 for v1, v2 in zip(nums2, sorted(nums)))
    
    # 72 ms, 83.64%. Time and Space: O(N)
    #   left         right
    # [......max] [min......]
    # if max > min, these 2 cannot be mixed, else, we have a split point. 
    def maxChunksToSorted(self, arr: List[int]) -> int:
        prefix_max = list(itertools.accumulate(arr, max))
        
        chunks = 0
        minimum = float("inf")
        for i, val in enumerate(reversed(arr)):
            if minimum >= prefix_max[~i]:
                chunks += 1
            minimum = min(minimum, val)
        return chunks
    
    # 76 ms, 72.21%. Time and Space: O(N). Same as above but pythonic
    def maxChunksToSorted(self, arr: List[int]) -> int:
        prefix_max = list(itertools.accumulate(arr, max))
        postfix_min = list(reversed(list(itertools.accumulate(arr[::-1], min, initial=float("inf")))))
        return sum(mx <= mn for mx, mn in zip(prefix_max, postfix_min[1:]))
# @lc code=end

