#
# @lc app=leetcode id=845 lang=python3
#
# [845] Longest Mountain in Array
#

# @lc code=start
# TAGS: Two Pointers
class Solution:
    # 160 ms, 85.39%
    def longestMountain(self, A: List[int]) -> int:
        length = state = 1; ans = 0
        for m1, m2 in zip(A, A[1:]):
            if state == 1: # not a mountain
                if m1 >= m2:  continue
                state = 2
                
            if state == 2: # increasing step
                if m1 < m2:
                    length += 1
                elif m1 > m2:
                    length += 1
                    ans = max(ans, length)
                    state = 3
                else:
                    length = 1
                    state = 1
                    
            elif state == 3: # decreasing step
                if m1 < m2:
                    length = 2
                    state = 2
                elif m1 > m2:
                    length += 1
                else:
                    length = 1
                ans = max(ans, length)
        return ans if ans > 1 else 0

    # clean solution from lee215. 
    def longestMountain(self, A):
        res = up = down = 0
        for i in range(1, len(A)):
            if down and A[i - 1] < A[i] or A[i - 1] == A[i]: 
                up = down = 0
            up += A[i - 1] < A[i]
            down += A[i - 1] > A[i]
            if up and down: res = max(res, up + down + 1)
        return res
# @lc code=end

