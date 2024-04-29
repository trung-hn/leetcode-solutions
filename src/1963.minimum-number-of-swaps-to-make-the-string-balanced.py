#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#


# @lc code=start
# TAGS: Two Pointers,String,Stack,Greedy
class Solution:
    # After realization: 1 swap reduce 2 pairs (4 chars)
    # Time: O(N). Space: O(1)
    def minSwaps(self, s: str) -> int:
        op = cl = 0
        for c in s:
            if c == "[":
                op += 1
            elif c == "]" and op:
                op -= 1
            else:
                cl += 1
        return (cl + op + 2) // 4  # trick to account for (sum % 4 == 0)


# @lc code=end
