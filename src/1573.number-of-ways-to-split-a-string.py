#
# @lc app=leetcode id=1573 lang=python3
#
# [1573] Number of Ways to Split a String
#

# @lc code=start
# TAGS: String
# REVIEWME: Paxton
class Solution:
    # 300 ms 29.38%. Time and Space: O(N)
    def numWays(self, s: str) -> int:
        ones = sum(c == '1' for c in s)
        if ones % 3: return 0
        if ones == 0:
            N = len(s) - 2
            return N * (N + 1) // 2 % (10**9 + 7)
        target = ones // 3
        N = len(s)
        
        left1 = left2 = None
        cnt = 0
        for i, c in enumerate(s):
            if c == '1':cnt += 1
            if cnt == target:
                if left1 is None: left1 = i
                left2 = i
        
        right1 = right2 = None
        cnt = 0
        for i, c in enumerate(s[::-1]):
            if c == '1': cnt += 1
            if cnt == target:
                if right1 is None: right1 = N - 1 - i
                right2 = N - 1 - i
        ans = (left2 - left1 + 1) * (right1 - right2 + 1) 
        return ans % (10**9 + 7)
    
    # 184 ms, 59.36%. Same as above but cleaner. 
    def numWays(self, s: str) -> int:
        ones = sum(c == '1' for c in s)
        if ones % 3: 
            return 0
        if ones == 0:
            N = len(s) - 2
            return N * (N + 1) // 2 % (10**9 + 7)
        
        target = ones // 3
        indexes = [i for i, c in enumerate(s) if c == '1']
        ans = (indexes[target] - indexes[target - 1]) * (indexes[-target] - indexes[~target])
        return ans % (10**9 + 7)
          
# @lc code=end

