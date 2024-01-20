#
# @lc app=leetcode id=1995 lang=python3
#
# [1995] Count Special Quadruplets
#

# @lc code=start
# TAGS: Array, Enumeration
class Solution:
    # Time: O(N^2). Space: O(N^2)
    def countQuadruplets(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        mem = collections.defaultdict(int)
        mem[nums[-1] - nums[-2]] = 1 # last pair d - c

        # find pair such that a + b = d - c
        for b in reversed(range(N - 2)):
            
            # Sum based on seen d - c
            for a in reversed(range(b)):
                left = nums[a] + nums[b]
                ans += mem[left]
            
            # Calculate d - c for the next a + b. d > c > b
            for d in range(b + 1, N):
                right = nums[d] - nums[b] # b is acting as c
                mem[right] += 1
            print(mem, ans)
        return ans
        
# @lc code=end

