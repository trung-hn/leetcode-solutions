#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
# TAGS: Hash Talble, Two Pointers, Sliding Window
# REVIEWME: Hash Talble, Two Pointers, Sliding Window


class Solution:
    # Two Sliding Window. Key: Exactly K = At Most(K) - at Most(K - 1)
    # Similar to lee215
    # 624 ms, 32.19%. Time: O(N). Space: O(N)
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def at_most(K):
            counter = collections.Counter()
            unique = ptr = total = 0
            for i, val in enumerate(A):
                counter[val] += 1
                if counter[val] == 1:
                    unique += 1
                while unique > K:
                    counter[A[ptr]] -= 1
                    if counter[A[ptr]] == 0:
                        unique -= 1
                    ptr += 1
                total += i - ptr + 1
                # The Above is trickiest part. Think about it this way:
                # [1] has 1 subarray with at most 1 unique
                # [1, 2] has 2 MORE subarray with at most 1 unique
                # [1, 2, 3] has 3 MORE subarray with at most 1 unique
                # For each new number, number of subarray increases by new length
                # Keep doing this until we reset our subarray
            return total
        return at_most(K) - at_most(K - 1)
# @lc code=end
