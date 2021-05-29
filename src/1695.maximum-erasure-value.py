#
# @lc app=leetcode id=1695 lang=python3
#
# [1695] Maximum Erasure Value
#

# @lc code=start
# TAGS: Two Pointers.


class Solution:
    # 1216 ms, 91.76%. Time: O(N). Space: O(1)
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visited = set()
        curr = ans = ptr = 0
        for num in nums:
            # If we see this before, move ptr
            while num in visited:
                curr -= nums[ptr]
                visited.discard(nums[ptr])
                ptr += 1
            # Update curr and ans
            curr += num
            visited.add(num)
            ans = max(ans, curr)
        return ans

    # Second sollution after a while.
    # 1328 ms, 48.07%. Time: O(N). Space: O(1)
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        ans = curr = start = 0
        for num in nums:
            # Update counter and total
            counter[num] += 1
            curr += num
            # While counter of current number > 1
            while counter[num] > 1:
                # Update counter, curr and move start
                counter[nums[start]] -= 1
                curr -= nums[start]
                start += 1
            ans = max(ans, curr)
        return ans
# @lc code=end
