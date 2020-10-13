#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
# TAGS: String
# REVIEWME: Pythonic
class Solution:
    # 28 m, 92.07%. Time: O(N). Space: O(1)
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        
        diff = [i for i, (c1, c2) in enumerate(zip(A, B)) if c1 != c2]
        if len(diff) > 2 or len(diff) == 1 : return False
        if len(diff) == 0: 
            return any(freq > 1 for freq in collections.Counter(A).values())
        return set([A[diff[0]], A[diff[1]]]) == set([B[diff[0]], B[diff[1]]])
        
    # Similar but clean code from lee215
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if A == B and len(set(A)) < len(A): return True
        diff = [(c1, c2) for c1, c2 in zip(A, B) if c1 != c2]
        return len(diff) == 2 and diff[0] == diff[1][::-1]

# @lc code=end

