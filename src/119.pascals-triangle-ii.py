#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
# TAGS: Array
class Solution:
    # 36 ms, 75%
    def getRow(self, rowIndex: int) -> List[int]:
        rv = [1]
        for i in range(rowIndex):
            rv = [1] + [sum(rv[i : i+2]) for i in range(len(rv)-1)] + [1]
        return rv
    
    # Time: O(k^2). Space: O(k)
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        prev = [1]
        for _ in range(rowIndex):
            curr = [1]
            for v1, v2 in zip(prev, prev[1:]):
                curr.append(v1 + v2)
            curr.append(1)
            prev = curr[:]
        return curr

    # Same time complexity but more memory efficient
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for _ in range(rowIndex):
            ans.append(1)
            for i in range(len(ans) - 2, 0, -1):
                ans[i] += ans[i - 1]
        return ans
# @lc code=end

