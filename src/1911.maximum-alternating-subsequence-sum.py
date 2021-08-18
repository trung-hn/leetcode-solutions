#
# @lc app=leetcode id=1911 lang=python3
#
# [1911] Maximum Alternating Subsequence Sum
#

# @lc code=start
# TAGS: Array, Dynamic Programming, Greedy


class Solution:
    # 996 ms, 99.7%. Time: O(N). Space: O(N). Greedy
    def maxAlternatingSum(self, nums: List[int]) -> int:
        seq = [nums[0]]
        inc = True
        for n1, n2 in zip(nums, nums[1:]):
            if (n2 > n1) == inc:
                seq[-1] = n2
            else:
                seq.append(n2)
                inc = not inc

        if len(seq) % 2 == 0:
            seq.pop()
        return sum(seq[::2]) - sum(seq[1::2])

    # just buy and sell at every turn just like stock
    # Time: O(N). Space: O(1)
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        for n1, n2 in zip(nums, nums[1:]):
            ans += max(0, n2 - n1)
        return ans
# @lc code=end
