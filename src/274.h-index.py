#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
# TAGS: Hash Table, Sort
class Solution:
    """
    There is an O(N) solution using counting sort. More in Article
    """
    # 32 ms 91%. Time: O(NlogN) because of sorting. Space: O(N)
    def hIndex(self, citations: List[int]) -> int:
        D = collections.Counter(citations)
        L = [[k, D[k]] for k in sorted(D, reverse=True)] + [[0, 0]]
        for i, (k, f) in enumerate(L):
            if f >= k: return k
            if f < k and f >= L[i+1][0]: return f # in case like this {3:2, 1:3}
            L[i + 1][1] += L[i][1]
        return 0
    
    # 32 ms 91%. Pythonic (from discussion). Time: O(NlogN) because of sorting. Space: O(N)
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < cit for i, cit in enumerate(sorted(citations, reverse = True)))
# @lc code=end

