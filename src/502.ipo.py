#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
# TAGS: Array, Greedy, Sorting, Heap
# REVIEWME: Greedy
class Solution:
    # Time: O(NlogN). Space: O(N)
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        The idea is to use 2 stack combined with a greedy approach:
        - Money always increase after a project.
        """
        projects = list(zip(capital, profits))
        heapq.heapify(projects)
        profits = []
        while k:
            while projects and w >= projects[0][0]:
                cap, prof = heapq.heappop(projects)
                heapq.heappush(profits, -prof)
            if profits:
                w -= heapq.heappop(profits)
            k -= 1
        return w

# @lc code=end

