#
# @lc app=leetcode id=1545 lang=python3
#
# [1545] Find Kth Bit in Nth Binary String
#

# @lc code=start
# TAGS: String
class Solution:
    """
    More solution from lee: https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/discuss/781181/JavaC%2B%2BPython-Iterative-Solutions
    """
    # 124 ms, 61.68 %. Time and Space: O(N^2) because as n grows, the number of digit doubles. 
    def findKthBit(self, n: int, k: int) -> str:
        S = '0'
        for _ in range(n):
            L = len(S) 
            num = f"{~int(S, 2) % (1 << L) :b}"
            S += '1' + num[::-1]
        return S[k-1]
# @lc code=end

