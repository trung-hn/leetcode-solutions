#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#

# @lc code=start
# TAGS: Greedy, Sliding Window
class Solution:
    # LTE. Time and Space O(N^2). 
    def minOperations(self, nums: List[int], x: int) -> int:
        q = [(x, 0, len(nums) - 1)]
        visited = {}
        depth = 0
        while q:
            cur = []
            for x, left, right in q:
                if x == 0: return depth
                if (left, right) in visited and visited[(left, right)] <= depth: continue
                visited[(left, right)] = depth
                if x < 0 or left > right:
                    continue
                cur.append((x - nums[left], left + 1, right))
                cur.append((x - nums[right], left, right - 1))
            depth += 1
            q = cur
        return -1
    
    # Think in reverse, instead of finding the minmum prefix + suffix, we can find the subarray with maximum length
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        y = prefix_sum[-1] - x
        
        ans = -1
        visited = {}
        for i, num in enumerate(prefix_sum):
            if y + num not in visited:
                visited[y + num] = i
            if num in visited:
                ans = max(ans, i - visited[num])
        if ans == -1: return -1
        return len(nums) - ans
# @lc code=end

