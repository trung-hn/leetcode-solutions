#
# @lc app=leetcode id=1513 lang=python3
#
# [1513] Number of Substrings With Only 1s
#

# @lc code=start
# TAGS: String, Math
import collections
class Solution:
    # 128 ms, 31.21 %. Time and Space: O(N) 
    # not optimal because we have to calculate the combination table
    def numSub(self, s: str) -> int:
        # Find the frequencies of each length of substring.
        freq = collections.defaultdict(int)
        cnt = 0
        s += '0'
        for c1, c2 in zip(s, s[1:]):
            if c1 == '1':
                cnt += 1
                if c1 != c2:
                    freq[cnt] += 1
            elif c1 == '0':
                cnt = 0

        # Generate combination table
        # 1: 1                   = 1
        # 2: 1 + 2               = 3
        # 3: 1 + 2 + 3           = 6
        # 4: 1 + 2 + 3 + 4       = 10
        # 5: 1 + 2 + 3 + 4 + 5   = 15
        combination = [0]
        for i in range(1, len(s) + 1):
            combination.append(combination[-1] + i)

        total = 0
        for k, v in freq.items():
            total += combination[k] * v
        return total % (10**9 + 7)

    # 84 ms, 65.37 %. Time and Space: O(N). Similar to above but more optimized. 
    def numSub(self, s: str) -> int:
        freq = collections.defaultdict(int)
        cnt = 0
        s += '0'
        for c1, c2 in zip(s, s[1:]):
            if c1 == '1':
                cnt += 1
                if c1 != c2:
                    freq[cnt] += 1
            elif c1 == '0':
                cnt = 0

        total = 0
        for k, v in freq.items():
            total += (k + 1) * k // 2 * v
        return total % (10**9 + 7)

# @lc code=end

