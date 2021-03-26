#
# @lc app=leetcode id=916 lang=python3
#
# [916] Word Subsets
#

# @lc code=start
# TAGS: String


class Solution:
    # 1060 ms, 41.94%. Time: O(A_t + B_t). Space: O(L). L = len(A) + len(B)
    # A_t is total amount of information in A
    # B_t is total amount of information in B
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        Bc = collections.Counter()
        for b in B:
            Bc |= collections.Counter(b)
        return [a for a in A if not Bc - collections.Counter(a)]

# @lc code=end
