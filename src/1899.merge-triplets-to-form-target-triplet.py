#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#

# @lc code=start
# TAGS: Greedy, Array


class Solution:
    """
    Approach: 
    only consider valid triplets where all numbers are less than target
    """
    # 19996 ms, 80.43%. Time: O(N). Space: O(1)

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a0, b0, c0 = target
        cnt = [0, 0, 0]
        for a, b, c in triplets:
            if a <= a0 and b <= b0 and c <= c0:
                if a == a0:
                    cnt[0] = 1
                if b == b0:
                    cnt[1] = 1
                if c == c0:
                    cnt[2] = 1
        return 0 not in cnt

# @lc code=end
