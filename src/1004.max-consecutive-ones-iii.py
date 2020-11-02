#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
# TAGS: Sliding Window, Two Pointers
class Solution:
    # 6465 ms, 5.02%. Time: O(N^2). Space: O(N)
    def longestOnes(self, A: List[int], K: int) -> int:
        
        def sum_from_i(i, K):
            k = K
            rv = 0
            for val, length in group[i:]:
                if val == 1:
                    rv += length
                elif val == 0 and length <= k:
                    k -= length
                    rv += length
                elif val == 0 and length > k:
                    rv += k
                    k = 0
                    break
            return rv, k
        
        group = [(i, len(list(g))) for i, g in itertools.groupby(A)]
        
        ans = 0
        for i in range(len(group)):
            rv, k = sum_from_i(i, K)
            if i > 0 and group[i - 1][1] > k:
                rv += k
            ans = max(ans, rv)
            
        return ans
    # 552 ms, 94.19%. Time: O(N). Space: O(1). Sliding Window
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        for right in range(len(A)):
            K -= 1 - A[right]
            if K < 0:
                K += 1 - A[left]
                left += 1
                
        # we can return this because we never decrease the size, only increase of not change.
        return right - left + 1

# @lc code=end

