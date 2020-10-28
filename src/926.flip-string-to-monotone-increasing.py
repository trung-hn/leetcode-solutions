#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#

# @lc code=start
# TAGS: Array
# REVIEWME: Array
class Solution:
    # 64 ms, 68.21%. Time and Space: O(N)
    def minFlipsMonoIncr(self, S: str) -> int:
        prefix_sum_1 = [0]
        for c in S:
            if c == '0': 
                prefix_sum_1.append(prefix_sum_1[-1])
            else:
                prefix_sum_1.append(prefix_sum_1[-1] + 1)
        
        postfix_sum_0 = [0]
        for c in reversed(S):
            if c == '1': 
                postfix_sum_0.append(postfix_sum_0[-1])
            else:
                postfix_sum_0.append(postfix_sum_0[-1] + 1)
        postfix_sum_0.reverse()
        return min(v1 + v2 for v1, v2 in zip(prefix_sum_1, postfix_sum_0))
    
    # Pythonic. Time and Space: O(N)
    def minFlipsMonoIncr(self, S: str) -> int:
        prefix_sum_1 = itertools.accumulate(S, lambda a, b: int(a) + int(b), initial = 0)
        postfix_sum_0 = [0]
        for c in reversed(S):
            postfix_sum_0.append(postfix_sum_0[-1] + int(c == '0'))
        postfix_sum_0.reverse()
        return min(v1 + v2 for v1, v2 in zip(prefix_sum_1, postfix_sum_0))  
# @lc code=end

