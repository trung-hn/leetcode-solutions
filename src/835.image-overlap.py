#
# @lc app=leetcode id=835 lang=python3
#
# [835] Image Overlap
#

# @lc code=start
# TAGS: Array
class Solution:
    """Other soltions:
    for sparse matrix from lee215:
    https://leetcode.com/problems/image-overlap/discuss/130623/C%2B%2BJavaPython-Straight-Forward

    using convolution, same complexity
    https://leetcode.com/problems/image-overlap/discuss/832150/Python-2-lines-using-convolutions-explained
    """
    # 600 ms, 41.56 %. Time: O(N^2). Space: O(N). N = R*C
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        def overlap(r, c):
            totalA = totalB = 0 
            for i in range(r):
                for j in range(c):
                    totalA += A[i][j] * B[R - r + i][C - c + j]
                    totalB += B[i][j] * A[R - r + i][C - c + j]
            return max(totalA, totalB)
        
        R, C = len(A), len(A[0])
        ans = 0
        for r in range(R):
            for c in range(C):
                ans = max(ans, overlap(r + 1, c + 1)) 
        return ans
# @lc code=end

