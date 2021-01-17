#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
# TAGS: Heap
class Solution:
    # 56 ms, 97%. O(N logN) because of sort
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]
    
    # 72 ms, 40%. Heap. ConnectionRefusedError(N logK) because each heap action takes logK and we perform N actions. 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numbers = []
        for num in nums:
            if len(numbers) < k:
                heapq.heappush(numbers, num)
            else:
                heapq.heappushpop(numbers, num)
        return heapq.heappop(numbers)
    
    # # 52 ms, 99%. O(N logK). Pythonic. Using nlargest from heapq. List is sorted from greatest to smallest
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
# @lc code=end

