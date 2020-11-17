#
# @lc app=leetcode id=1652 lang=python3
#
# [1652] Defuse the Bomb
#

# @lc code=start
# TAGS: Array
class Solution:
    # 36 ms, 89.49%. Time and Space: O(N)
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0: 
            return [0] * len(code)
        if k < 0: 
            k = -k
            code = code[-k:] + code[:-1]
        else:
            code = code[1:] + code[:k]
            
        prefix = [sum(code[:k])]
        for i in range(k, len(code)):
            prefix.append(prefix[-1] + code[i] - code[i - k])
        return prefix
    
    # 24 ms, 99.89%. Clean solution from discussion.
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k < 0: return self.decrypt(code[::-1], -k)[::-1]
        n = len(code)
        prefix = code * 2
        for i in range(2 * n):
            prefix[i] += i > 0 and prefix[i - 1]
            if k <= i < n + k:
                code[i - k] = prefix[i] - prefix[i - k]
        return code
        
# @lc code=end

