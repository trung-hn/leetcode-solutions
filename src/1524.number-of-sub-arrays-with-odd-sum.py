#
# @lc app=leetcode id=1524 lang=python3
#
# [1524] Number of Sub-arrays With Odd Sum
#

# @lc code=start
# TAGS: Array, Math, Dynamic Programming
# REVIEWME: Good Problem
class Solution:
    # LTE. Time: O(N^2). Space: O(N)
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        total = 0
        for i in range(len(prefix)):
            for j in range(i + 1, len(prefix)):
                if (prefix[j] - prefix[i]) % 2:
                    total += 1
        return total % (10**9 + 7)

    # 1456 ms, 54.16 %. Time: O(N). Space: O(N). Need 2 Hints to solve
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        total = 0
        evens = odds = 0
        for num in prefix:
            if num % 2: 
                total += evens
                odds += 1
            else: 
                total += odds
                evens += 1
        return total % (10**9 + 7)

    # 1260 ms, 90.02 %. Time: O(N). Space: O(1). Similar to above but 1 pass.
    def numOfSubarrays(self, arr: List[int]) -> int:
        total = prefix = odds = 0 
        evens = 1 # This is due to the first '0'
        for num in arr:
            prefix += num
            if prefix % 2: 
                total += evens
                odds += 1
            else: 
                total += odds
                evens += 1
        return total % (10**9 + 7)
        
    # 1196 ms, 99.89 %. Even Cleaner solution. From Discussion
    def numOfSubarrays(self, arr: List[int]) -> int:
        total = odds = evens = 0
        for num in arr:
            evens += 1
            if num % 2:
                odds, evens = evens, odds
            total += odds
        return total % (10**9 + 7)

# @lc code=end