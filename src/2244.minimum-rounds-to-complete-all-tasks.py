#
# @lc app=leetcode id=2244 lang=python3
#
# [2244] Minimum Rounds to Complete All Tasks
#


# @lc code=start
# TAGS: Array, Hash Table, Greedy, Counting
import collections


class Solution:
    # 726 ms, 58.88%.
    # Time and Space: O(N)
    def minimumRounds(self, tasks: List[int]) -> int:
        freqs = collections.defaultdict(int)
        for task in tasks:
            freqs[task] += 1

        ans = 0
        for task, freq in freqs.items():
            if freq == 1:
                return -1

            # Derived from simulation
            if freq % 3 == 0:
                ans += freq // 3
            else:
                ans += freq // 3 + 1
        return ans


# @lc code=end
