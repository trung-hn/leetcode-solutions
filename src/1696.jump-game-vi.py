#
# @lc app=leetcode id=1696 lang=python3
#
# [1696] Jump Game VI
#

# @lc code=start
# TAGS: Dequeue
# REVIEWME: Dequeue, Monotonic Dequeue


class Solution:

    # TLE. Time: O(N*K). Space: O(N). Memoization
    def maxResult(self, nums: List[int], k: int) -> int:
        @cache
        def dfs(start=0):
            if start == len(nums) - 1:
                # Key point to make sure we arrive at last cell
                return nums[-1]
            if start >= len(nums):
                return 0
            rv = float("-inf")
            for i in range(start + 1, start + k + 1):
                rv = max(rv, dfs(i) + nums[start])
            return rv
        return dfs()

    # TLE. Time: O(N*K). Space: O(N). Custom Memoization
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [float("-inf")] * len(nums)
        dp[-1] = nums[-1]  # Key point to make sure we arrive at last cell

        def dfs(start=0):
            if dp[start] != float("-inf"):
                return dp[start]
            if start >= len(nums):
                return 0
            for i in range(start + 1, min(start + k + 1, len(nums))):
                dp[start] = max(dp[start], dfs(i) + nums[start])
            return dp[start]
        return dfs()

    # Advance Solution from discussion. Use Q to keep track of max of the window size k
    # 1200 ms, 18.45%. Time and Space: O(N). Monotonic Queue
    def maxResult(self, nums: List[int], k: int) -> int:
        deq = collections.deque([0])
        for i in range(1, len(nums)):

            # Outdated data because window size is k
            if deq and deq[0] < i - k:
                deq.popleft()

            # This is the max of the window size k
            nums[i] += nums[deq[0]]

            # Maintain monotonic queue
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)
        return nums[-1]
# @lc code=end
