#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#

# @lc code=start
# TAGS: Hash Table, Math, Dynamic Programming.


class Solution:
    """
    DP with Hash Table.
    """
    # 532 ms, 77.89%. Time and Space: O(N)

    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        visited = collections.defaultdict(int)
        for num in arr:
            visited[num] = visited[num - diff] + 1
        return max(visited.values())

# @lc code=end
