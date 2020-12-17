#
# @lc app=leetcode id=1653 lang=python3
#
# [1653] Minimum Deletions to Make String Balanced
#

# @lc code=start
# TAGS: Greedy, String
# REVIEWME: Greedy, String
class Solution:
    # 804 ms, 52.52%. Time and Space: O(N)
    def minimumDeletions(self, s: str) -> int:
        total_a = s.count("a")
        b_sofar = a_sofar = 0
        A = []; B = []
        for c in s:
            if c == "b": 
                b_sofar += 1
                B.append(total_a - a_sofar)
            else: 
                a_sofar += 1
                A.append(b_sofar)
        B.reverse()
        
        a_deleted = b_deleted = 0
        while A and B:
            if A[-1] - b_deleted == B[-1] - a_deleted == 0: 
                break
            elif A[-1] - b_deleted >= B[-1] - a_deleted:
                A.pop()
                a_deleted += 1
            else:
                B.pop()
                b_deleted += 1
        return a_deleted + b_deleted
# @lc code=end

