#
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#

# @lc code=start
# TAGS: Array


class Solution:
    """
    Approach: Get min and minIdx from the right
    Get max_sofar from the left, when max_sofar < min => return

    There is a O(1) Space solution in the discussion
    """

    # 184 ms, 72.73%. Time and Space: O(N). 2 passes
    def partitionDisjoint(self, A: List[int]) -> int:

        # Get min, idx from the right
        mins = [A[-1]] * len(A)
        for i in reversed(range(len(A) - 1)):
            mins[i] = min(mins[i + 1], A[i])

        # when max_sofar > mins[i], we got our result
        max_sofar = A[0]
        for i, num in enumerate(A):
            max_sofar = max(num, max_sofar)
            if max_sofar <= mins[i + 1]:
                return i + 1

# @lc code=end
