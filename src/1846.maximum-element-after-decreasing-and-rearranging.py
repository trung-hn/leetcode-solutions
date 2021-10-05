#
# @lc app=leetcode id=1846 lang=python3
#
# [1846] Maximum Element After Decreasing and Rearranging
#

# @lc code=start
# TAGS: Array, Greedy, Sorting


class Solution:
    # 596 ms, 20.37%. Time and Space: O(N).
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Number freq
        counter = collections.Counter(arr)
        # Numbers that are > len(arr). these are only used for filling in missing number.
        available = sum(n > len(arr) for n in arr)
        i = ans = len(arr)
        while i > 0:
            # This number is not in arr
            if not counter[i]:
                # Use another number to fill in its place. If we cannot, we have to decrease our max
                if available:
                    available -= 1
                else:
                    ans -= 1
            # Other occurences can be used for future.
            else:
                available += counter[i] - 1
            i -= 1
        return ans

# @lc code=end
