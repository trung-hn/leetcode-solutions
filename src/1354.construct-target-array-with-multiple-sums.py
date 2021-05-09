#
# @lc app=leetcode id=1354 lang=python3
#
# [1354] Construct Target Array With Multiple Sums
#

# @lc code=start
# TAGS: Greedy, Heap
# REVIEWME: Greedy, Hard

import heapq


class Solution:
    """
    Approach:
    Work backward from the largest value.
    We know largest = sum(rest) + diff => largest > sum(rest)
    Thus, we can find the number that largest replace
    """
    # 252 ms, 74.45%. Time: O(NlogN). Space: O(N)

    def isPossible(self, target: List[int]) -> bool:
        # Edge case
        if len(target) == 1:
            return target == [1]
        # Init Heap
        heap = [-num for num in target]
        heapq.heapify(heap)
        total = sum(target)
        while total != len(target):
            largest = -heapq.heappop(heap)

            # largest cannot be <= sum(the rest)
            if largest <= total - largest:
                return False

            # The value that largest replaced
            remain = largest % (total - largest)

            # Edge case: remain = 0 but init array start with only 1s
            if remain == 0:
                remain = total - largest

            # Update total and heap
            total = total - largest + remain
            heapq.heappush(heap, -remain)
        return True
# @lc code=end
