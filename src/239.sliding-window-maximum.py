#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
# TAGS:  Monotonic Dequeue, Sliding Window, Heap
# REVIEWME:  Monotonic Dequeue, Sliding Window, Heap
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        ans = []
        for i, num in enumerate(nums):
            while q and q[-1] < num:
                q.pop()
            q.append(num)
            
            if i < k - 1: continue    
            ans.append(q[0])
            if q[0] == nums[i - k + 1]: 
                q.popleft()
        return ans
# @lc code=end

