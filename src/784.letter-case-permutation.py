#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start
# TAGS: Backtracking, Bit Manipulation
class Solution:
    # 48 ms, 95.78%. Time and Space: O(2^N)
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [""]
        for c in S.lower():
            temp = []
            for prev in ans:
                temp.append(prev + c)
            if c.isalpha():
                for prev in ans:
                    temp.append(prev + c.upper())
            ans = temp
        return ans
    
    # 44 ms, 98%. Pythonic solution from lee
    def letterCasePermutation(self, S):
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*L)]
# @lc code=end

