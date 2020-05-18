#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
# TAGS: String, Two Pointers, Sliding Window
class Solution:
    """
    100 ms, 34.95%. Time: O(S1 + S2), Space: O(52) = O(1)
    Approach: try Counter first, then use array instead
    Use sliding windows
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def are_equal(C1, C2):
            return all(c1 == c2 for c1, c2 in zip(C1, C2))
        C1 = [0] * 26
        C2 = [0] * 26
        
        for c1 in s1:
            C1[ord(c1) - ord('a')] += 1
        
        for i, c2 in enumerate(s2):
            C2[ord(c2) - ord('a')] += 1
            if i >= len(s1) - 1:
                if are_equal(C1, C2): 
                    return True
                C2[ord(s2[i - len(s1) + 1]) - ord('a')] -= 1
        return False
# @lc code=end

