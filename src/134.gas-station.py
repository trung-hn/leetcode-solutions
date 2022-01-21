#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
# TAGS: Greedy
# REVIEWME: Dynamic Programming, Greedy
from typing import List


class Solution:
    # 68 ms, 31.09%. O(N) Time and Space
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas:
            return -1
        net = [g-d for g, d in zip(gas, cost)]
        net2 = net + net[:-1]
        # Greatest sub array sum.
        greatest = curr = 0
        ptr = i_max = 0
        for i, num in enumerate(net2):
            curr += num
            if curr > greatest:
                greatest = curr
                i_max = ptr
            if curr < 0:
                curr = 0
                ptr = i + 1
        # Start moving to determine if we can make a loop
        tank = net[i_max]
        location = i_max
        while tank >= 0:
            location = (location + 1) % len(net)
            if location == i_max:
                return i_max
            tank += net[location]
        return -1

    # Combine into 1 step
    # 52 ms, 75.93%
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas:
            return -1

        total = curr = 0
        start = 0
        for i in range(len(gas)):
            curr += gas[i] - cost[i]
            total += gas[i] - cost[i]

            # Think this way:
            # If we are out of gas. We might as wells restart at the next station
            if curr < 0:
                curr = 0
                start = i + 1

        return start if total >= 0 else -1

    # 68 ms, 31.09%. O(N) Time and Space
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas:
            return -1
        if sum(gas) < sum(cost):
            return -1

        gas_diff = [g - c for g, c in zip(gas, cost)]
        gas_diff = gas_diff + gas_diff[:-1]
        curr = ptr = highest = 0
        for i, val in enumerate(gas_diff):
            if val > curr + val:
                ptr = i
            curr = max(val, curr + val)
            highest = max(highest, curr)
        return ptr

# @lc code=end
