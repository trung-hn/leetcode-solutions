#
# @lc app=leetcode id=1560 lang=python3
#
# [1560] Most Visited Sector in  a Circular Track
#

# @lc code=start
# TAGS: Array
# REVIEWME: Brain Teaser
class Solution:
    # 60 ms, 77.86 %. Time and Space: O(N). Only care about the last loop. 
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        starting_point = rounds[0]
        
        last_round = 0
        for i in range(1, len(rounds)):
            if rounds[i] == starting_point:
                last_round = i

        cnts = [0] * n
        for val1, val2 in zip(rounds[last_round:], rounds[last_round + 1:]):
            if val1 < val2:
                for val in range(val1, val2):
                    cnts[val - 1] += 1
            else:
                for val in range(val1, val2 + n):
                    cnts[val % n - 1] += 1
        
        cnts[rounds[-1] - 1] += 1

        mx = max(cnts)
        return [i + 1 for i, val in enumerate(cnts) if val == mx]

    # Inspired from lee215. We only need to care about start and end. 
    #                 s ----- n
    # 1 --------------------- n
    # 1 --------------------- n
    # 1 ----- e
    # 36 ms, 98.91 %. Time: O(N). Space: O(1)
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return range(start, end + 1)
        else:
            return list(range(1, end + 1)) + list(range(start, n + 1))
# @lc code=end