#
# @lc app=leetcode id=3075 lang=python3
#
# [3075] Maximize Happiness of Selected Children
#


# @lc code=start
# TAGS: Array, Greedy, Sorting
class Solution:
    # Time: O(NlogK). Space: O(K)
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        heap = []
        for hap in happiness:
            heapq.heappush(heap, hap)
            if len(heap) > k:
                heapq.heappop(heap)
        ans = 0
        while heap:
            ans += max(0, heapq.heappop(heap) - len(heap))
        return ans

    # worst complexity but faster due to built-in sort
    # Time: O(NlogN). Space: O(N)
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        return sum(max(0, happiness.pop() - i) for i in range(k))


# @lc code=end
