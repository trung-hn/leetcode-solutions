#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start
# TAGS: Two Pointers
class Solution:
    """
    Time: O(N + M) | Space: O(1)
    """
    # 144 ms, 99.05%. First sol
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []
        while i < len(A) and j < len(B):
            start1, end1 = A[i]
            start2, end2 = B[j]
            if start1 > end2: 
                j += 1
                continue
            elif start2 > end1:
                i += 1
                continue
            ans.append((max(start1, start2), min(end1, end2)))
            if end2 > end1:
                i += 1
            else:
                j += 1
        return ans
    # 144 ms, 99.05%. Cleaner solution
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []
        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ans    
# @lc code=end

