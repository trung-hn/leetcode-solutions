#
# @lc app=leetcode id=833 lang=python3
#
# [833] Find And Replace in String
#

# @lc code=start
# TAGS: String
class Solution:
    # 28 ms, 98.48%. Time: O(NlogN). Space: O(N)
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        ans = []
        prev = 0
        for i, s, t in sorted(zip(indexes, sources, targets)):
            ans.append(S[prev:i])
            prev = i + len(s)
            if S[i:].startswith(s):
                ans.append(t)
            else:
                prev = i
            
        ans.append(S[prev:])
        return "".join(ans)
    
    # 28 ms, 98.48%. Time and Space: O(N)
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        ans = list(S)
        for i, s, t in zip(indexes, sources, targets):
            if S[i:].startswith(s):
                ans[i] = t
                for j in range(i + 1, len(s) + i):
                    ans[j] = ""
        return "".join(ans)
            
# @lc code=end

