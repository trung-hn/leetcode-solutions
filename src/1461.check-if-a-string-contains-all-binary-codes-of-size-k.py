#
# @lc app=leetcode id=1461 lang=python3
#
# [1461] Check If a String Contains All Binary Codes of Size K
#

# @lc code=start
# TAGS: String, Bit Manipulation
# REVIEWME: String


class Solution:
    # 496 ms, 38.40%. Time: O(N). Space: O(2**K)
    def hasAllCodes(self, s: str, k: int) -> bool:
        visited = set()
        for i in range(len(s) - k + 1):
            sub = s[i: i + k]
            visited.add(int(sub, 2))
        return len(visited) == 1 << k

    # lee215 follow up questions. subsequence intead of substring
    # Approach: find a pair of '01' greedy. This will reduce k by 1
    def hasAllCodes2(self, s: str, k: int) -> bool:
        i, n = 0, len(s)
        while i < n and k > 0:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            k -= 1 if j < n else 0
            i = j + 1
        return k == 0
# @lc code=end
