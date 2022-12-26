#
# @lc app=leetcode id=2389 lang=python3
#
# [2389] Longest Subsequence With Limited Sum
#

# @lc code=start
# TAGS: Array, Binary Search, Greedy, Sorting, Prefix Sum
class Solution:
    # Time: O(NlogN). Space: O(N)
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        print(prefix)
        ans = []
        for query in queries:
            idx = bisect.bisect_right(prefix, query)
            ans.append(idx - 1)
        return ans


# @lc code=end
