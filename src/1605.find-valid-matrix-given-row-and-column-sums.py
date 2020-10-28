#
# @lc app=leetcode id=1605 lang=python3
#
# [1605] Find Valid Matrix Given Row and Column Sums
#

# @lc code=start
# TAGS: Greedy
class Solution:
    """
    This is a Greedy problem. Proof is not easy which can be found here:
    https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/discuss/876845/JavaC%2B%2BPython-Easy-and-Concise-with-Prove
    """
    # 1172 ms, 33.74%. Time:O(MN). Space:O(MN)
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        R, C = len(rowSum), len(colSum)
        ans = [[0] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                ans[r][c] = min(rowSum[r], colSum[c])
                rowSum[r] -= ans[r][c]
                colSum[c] -= ans[r][c]
        return ans
    
    # 684 ms, 96.81%. Time:O(MN). Space:O(MN). This is faster because process time is O(M+N)
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        R, C = len(rowSum), len(colSum)
        ans = [[0] * C for _ in range(R)]
        r = c = 0
        while r < R and c < C:
            ans[r][c] = min(rowSum[r], colSum[c])
            rowSum[r] -= ans[r][c]
            colSum[c] -= ans[r][c]
            if rowSum[r] == 0: r += 1
            if colSum[c] == 0: c += 1
                
        return ans
# @lc code=end

